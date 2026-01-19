"""
Quantitative evaluation using embedding similarity with ChromaDB.

This module evaluates survey quality by computing embedding similarities between
system-generated surveys and human-written surveys (ground truth).

For each system's survey, we:
1. Extract outline/content/reference entries
2. Generate embeddings for each entry
3. Find top-N most similar entries from Human surveys in ChromaDB
4. Calculate average similarity score

The similarity scores indicate how close the system output is to human quality.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from dotenv import load_dotenv

load_dotenv()

# Disable ChromaDB telemetry BEFORE importing chromadb
os.environ["ANONYMIZED_TELEMETRY"] = "False"

import chromadb
from openai import OpenAI
from tqdm import tqdm

# Disable verbose logs early
logging.getLogger("chromadb").setLevel(logging.WARNING)
logging.getLogger("chromadb.telemetry").setLevel(logging.CRITICAL)

# Ensure we can import pipeline classes
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from data_processing_pipeline import SurveyData  # type: ignore

# ----------------------------- Config ----------------------------- #


@dataclass
class QuantitativeEvalConfig:
    """Configuration for quantitative evaluation."""

    processed_dir: str = "results/processed"
    output_dir: str = "results/evaluation"
    chroma_db_dir: str = "chromadb_quantitative"

    # Systems to evaluate (e.g., ["Autosurvey", "Gemini"])
    systems: Optional[List[str]] = None
    # Categories to evaluate (e.g., ["Biology", "Computer Science"])
    categories: Optional[List[str]] = None

    # Embedding model
    embedding_model: Optional[str] = None
    embedding_api_key: Optional[str] = None
    embedding_api_base: Optional[str] = None

    # Top-N similar entries to retrieve for scoring (not used when use_ams=True)
    outline_top_n: int = 5
    content_top_n: int = 5
    reference_top_n: int = 5

    # Batch size for embedding generation
    batch_size: int = 10

    # Which parts to evaluate
    eval_outline: bool = True
    eval_content: bool = True
    eval_reference: bool = True

    # Resume from previous run
    resume_from: Optional[str] = None

    # Use Average Maximum Similarity (AMS) mode
    # When True:
    # - For reference/content: compute average of maximum similarity for each entry
    # - For outline: compute F1 score based on Precision (G->H) and Recall (H->G)
    # - top_n parameters are ignored
    use_ams: bool = False
    
    # Use bidirectional F1 for all aspects (outline/content/reference) in AMS mode
    # When True and use_ams=True:
    # - All aspects compute F1 score with precision (G→H) and recall (H→G)
    # When False and use_ams=True:
    # - Only outline computes F1, content/reference compute unidirectional AMS
    use_bidirectional_for_all: bool = False
    
    # Use threshold-based matching for precision/recall/F1 in AMS mode
    # When True:
    # - Count a match only if max similarity >= threshold
    # - Precision denominator is total generated entries
    # - Recall denominator is total Human entries
    use_threshold: bool = False
    outline_threshold: float = 0.7
    content_threshold: float = 0.7
    reference_threshold: float = 0.7
    
    # Use thresholded AMS for content/reference in AMS mode
    # When True:
    # - For each entry, max similarity below threshold is treated as 0
    # - Thresholds are aspect-specific
    use_thresholded_ams: bool = False

    def to_json(self, path: str) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(asdict(self), f, indent=2, ensure_ascii=False)

    @classmethod
    def from_json(cls, path: str) -> "QuantitativeEvalConfig":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(**data)


# ----------------------------- Embedding utilities ----------------------------- #


class EmbeddingClient:
    """Client for generating embeddings via OpenAI API."""

    def __init__(
        self,
        model: str,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
    ):
        self.model = model
        self.client = OpenAI(
            api_key=api_key or os.environ.get("OPENAI_API_KEY"),
            base_url=api_base or os.environ.get("OPENAI_API_BASE"),
        )
        self.logger = logging.getLogger(self.__class__.__name__)

    def embed_texts_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a batch of texts.

        Args:
            texts: List of texts to embed

        Returns:
            List of embedding vectors
        """
        try:
            response = self.client.embeddings.create(model=self.model, input=texts)
            embeddings = [data.embedding for data in response.data]
            self.logger.debug(
                f"Generated {len(embeddings)} embeddings "
                f"(tokens: {response.usage.total_tokens})"
            )
            return embeddings
        except Exception as exc:
            self.logger.error(f"Embedding error: {exc}")
            raise


# ----------------------------- ChromaDB helpers ----------------------------- #


def get_or_create_collection(
    client: chromadb.PersistentClient, name: str
) -> chromadb.Collection:
    """Get or create a ChromaDB collection with cosine distance metric."""
    try:
        return client.get_collection(name)
    except Exception:
        # Use cosine distance to ensure similarity scores are in [0, 1] range
        # cosine distance = 1 - cosine_similarity, so similarity = 1 - distance
        return client.create_collection(
            name=name,
            metadata={"hnsw:space": "cosine"}
        )


def collection_name_for(category: str, aspect: str, system: str = "Human") -> str:
    """
    Build collection name for a given category/aspect/system.

    Example: Biology_outline_Human
    """
    # Sanitize category name
    category = category.replace(" ", "_").replace(".", "").replace("-", "_")
    return f"{category}_{aspect}_{system}"


# ----------------------------- Data extraction ----------------------------- #


def extract_outline_texts(survey: SurveyData) -> List[str]:
    """
    Extract outline text representations.

    Each outline item title is treated as a separate entry.
    """
    outline_list = survey.outline.to_list()
    # Extract just the titles
    return [title for level, title in outline_list]


def extract_content_texts(survey: SurveyData) -> List[str]:
    """
    Extract content section texts.

    Each section is represented as: "heading: content..."
    """
    texts = []
    for section in survey.content.sections:
        text = f"{section.heading}: {section.content}"
        texts.append(text)
    return texts


def extract_reference_texts(survey: SurveyData) -> List[str]:
    """
    Extract reference texts.

    Each reference entry is a text string.
    """
    texts = []
    for ref in survey.references.entries:
        title = (ref.title or "").strip()
        text = (ref.text or "").strip()
        # Prefer title when available; fall back to raw text.
        texts.append(title or text)
    return texts


# ----------------------------- Index builder ----------------------------- #


class HumanIndexBuilder:
    """
    Builds ChromaDB indices for Human surveys (ground truth).
    """

    def __init__(
        self, config: QuantitativeEvalConfig, embedding_client: EmbeddingClient
    ):
        self.config = config
        self.embedding_client = embedding_client
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Create ChromaDB client with telemetry disabled
        settings = chromadb.config.Settings(
            anonymized_telemetry=False,
            allow_reset=True,
        )
        self.chroma_client = chromadb.PersistentClient(
            path=config.chroma_db_dir,
            settings=settings,
        )

    def build_indices(self) -> None:
        """
        Build ChromaDB collections for all Human surveys.

        For each category, we create three collections:
        - {category}_outline_Human
        - {category}_content_Human
        - {category}_reference_Human
        """
        human_dir = Path(self.config.processed_dir) / "Human"
        if not human_dir.exists():
            self.logger.warning(f"Human directory not found: {human_dir}")
            return

        # Get all categories
        categories = [d.name for d in human_dir.iterdir() if d.is_dir()]
        if self.config.categories:
            categories = [c for c in categories if c in self.config.categories]

        self.logger.info(f"Building indices for {len(categories)} categories")

        for category in categories:
            self.logger.info(f"Processing category: {category}")
            self._build_category_index(category)

    def _build_category_index(self, category: str) -> None:
        """Build index for a single category."""
        category_dir = Path(self.config.processed_dir) / "Human" / category
        files = list(category_dir.glob("*_split.json"))

        if not files:
            self.logger.warning(f"No files found in {category_dir}")
            return

        # Get or create collections
        outline_coll = get_or_create_collection(
            self.chroma_client, collection_name_for(category, "outline")
        )
        content_coll = get_or_create_collection(
            self.chroma_client, collection_name_for(category, "content")
        )
        reference_coll = get_or_create_collection(
            self.chroma_client, collection_name_for(category, "reference")
        )

        # Check which collections need to be built
        need_outline = outline_coll.count() == 0
        need_content = content_coll.count() == 0
        need_reference = reference_coll.count() == 0
        
        if not (need_outline or need_content or need_reference):
            self.logger.info(f"Category {category} already fully indexed, skipping")
            return
        
        self.logger.info(
            f"Building indices for {category}: "
            f"outline={need_outline}, content={need_content}, reference={need_reference}"
        )

        # Process all files
        all_outline_texts = []
        all_content_texts = []
        all_reference_texts = []

        self.logger.info(f"Processing {len(files)} files in {category}")
        for file_path in tqdm(files, desc=f"Reading {category} files", leave=False):
            survey = self._load_survey(file_path)

            if need_outline and self.config.eval_outline:
                all_outline_texts.extend(extract_outline_texts(survey))
            if need_content and self.config.eval_content:
                all_content_texts.extend(extract_content_texts(survey))
            if need_reference and self.config.eval_reference:
                all_reference_texts.extend(extract_reference_texts(survey))

        # Generate embeddings and add to collections
        if need_outline and all_outline_texts:
            self._add_to_collection(
                outline_coll, all_outline_texts, f"{category}_outline"
            )
        elif need_outline:
            self.logger.warning(f"No outline texts found in {category} Human files")

        if need_content and all_content_texts:
            self._add_to_collection(
                content_coll, all_content_texts, f"{category}_content"
            )
        elif need_content:
            self.logger.warning(f"No content texts found in {category} Human files")

        if need_reference and all_reference_texts:
            self._add_to_collection(
                reference_coll, all_reference_texts, f"{category}_reference"
            )
        elif need_reference:
            self.logger.warning(f"No reference texts found in {category} Human files")

    def _add_to_collection(
        self, collection: chromadb.Collection, texts: List[str], prefix: str
    ) -> None:
        """Add texts with embeddings to a collection."""
        self.logger.info(f"Adding {len(texts)} items to {collection.name}")

        batch_size = self.config.batch_size
        for i in tqdm(
            range(0, len(texts), batch_size),
            desc=f"Embedding {prefix}",
            leave=False,
        ):
            batch_texts = texts[i : i + batch_size]
            try:
                embeddings = self.embedding_client.embed_texts_batch(batch_texts)
                ids = [f"{prefix}_{i + j}" for j in range(len(batch_texts))]
                collection.add(
                    embeddings=embeddings, documents=batch_texts, ids=ids
                )
            except Exception as exc:
                self.logger.error(f"Failed to add batch {i}: {exc}")

    def _load_survey(self, json_path: Path) -> SurveyData:
        """Load survey from JSON file."""
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return SurveyData.from_dict(data)


# ----------------------------- Evaluator ----------------------------- #


class QuantitativeEvaluator:
    """
    Evaluates system surveys by computing embedding similarities with Human surveys.
    """

    def __init__(
        self, config: QuantitativeEvalConfig, embedding_client: EmbeddingClient
    ):
        self.config = config
        self.embedding_client = embedding_client
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Create ChromaDB client with telemetry disabled
        settings = chromadb.config.Settings(
            anonymized_telemetry=False,
            allow_reset=True,
        )
        self.chroma_client = chromadb.PersistentClient(
            path=config.chroma_db_dir,
            settings=settings,
        )
        self.output_file: Optional[Path] = None
        self.previous_results: Dict[str, Any] = self._load_previous_results()

    def _load_previous_results(self) -> Dict[str, Any]:
        """Load previous evaluation results if resume_from is specified."""
        if not self.config.resume_from:
            return {"by_system": {}}

        resume_path = Path(self.config.resume_from)
        if not resume_path.exists():
            self.logger.warning(f"Resume file not found: {resume_path}")
            return {"by_system": {}}

        try:
            with open(resume_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as exc:
            self.logger.warning(f"Failed to load resume file: {exc}")
            return {"by_system": {}}

    def _is_file_already_evaluated(
        self, file_path: Path, system: str, category: str
    ) -> bool:
        """Check if a file has already been evaluated."""
        system_data = self.previous_results.get("by_system", {}).get(system, {})
        category_data = system_data.get(category, {})
        files_data = category_data.get("files", [])

        file_str = str(file_path).replace("\\", "/")
        for entry in files_data:
            if entry.get("file", "").replace("\\", "/") == file_str:
                scores = entry.get("scores", {})
                if scores and any(scores.get(k) is not None for k in ["outline", "content", "reference"]):
                    return True
        return False

    def _save_summary_incremental(self, summary: Dict[str, Any]) -> None:
        """Save evaluation summary incrementally."""
        if not self.output_file:
            return
        try:
            with open(self.output_file, "w", encoding="utf-8") as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
        except Exception as exc:
            self.logger.error(f"Failed to save: {exc}")

    def evaluate(self) -> Dict[str, Any]:
        """
        Run quantitative evaluation for all configured systems.

        Returns:
            Summary dictionary with scores
        """
        # Determine systems to evaluate
        systems = self.config.systems or self._get_systems()
        systems = [s for s in systems if s != "Human"]  # Exclude Human

        # Initialize summary
        if self.config.resume_from and self.previous_results.get("by_system"):
            summary = self.previous_results.copy()
        else:
            summary = {"by_system": {}, "total": 0}

        # Set up output file
        Path(self.config.output_dir).mkdir(parents=True, exist_ok=True)
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        summary["generated_at"] = timestamp
        self.output_file = (
            Path(self.config.output_dir)
            / f"quantitative_evaluation_{timestamp}.json"
        )

        for system in systems:
            self.logger.info(f"Evaluating system: {system}")
            categories = self.config.categories or self._get_categories(system)

            if system not in summary["by_system"]:
                summary["by_system"][system] = {}

            for category in categories:
                self.logger.info(f"  Category: {category}")
                cat_results = self._evaluate_category(system, category, summary)

        # Final save
        summary["generated_at"] = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        summary["total"] = sum(
            len(cat_data.get("files", []))
            for sys_data in summary["by_system"].values()
            for cat_data in sys_data.values()
        )
        with open(self.output_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        self.logger.info(f"Saved evaluation to {self.output_file}")
        return summary

    def _evaluate_category(
        self, system: str, category: str, summary: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Evaluate all files in a system/category."""
        category_dir = Path(self.config.processed_dir) / system / category
        if not category_dir.exists():
            self.logger.warning(f"Directory not found: {category_dir}")
            return []

        files = list(category_dir.glob("*_split.json"))

        # Load existing results
        existing_results = []
        if self.config.resume_from:
            system_data = self.previous_results.get("by_system", {}).get(system, {})
            category_data = system_data.get(category, {})
            existing_results = category_data.get("files", [])

        results = list(existing_results)
        category_start = time.time()

        for file_path in tqdm(files, desc=f"Evaluating {system}/{category}"):
            if self._is_file_already_evaluated(file_path, system, category):
                continue

            try:
                result = self._evaluate_file(file_path, category)
                results.append(result)

                # Update summary incrementally
                if system not in summary["by_system"]:
                    summary["by_system"][system] = {}

                duration = round(time.time() - category_start, 2)
                summary["by_system"][system][category] = {
                    "files": results,
                    "averages": self._compute_averages(results),
                    "total_duration_seconds": duration,
                }
                summary["total"] = sum(
                    len(cat_data.get("files", []))
                    for sys_data in summary["by_system"].values()
                    for cat_data in sys_data.values()
                )
                self._save_summary_incremental(summary)

            except Exception as exc:
                self.logger.exception(f"Failed to evaluate {file_path}: {exc}")

        return results

    def _evaluate_file(self, file_path: Path, category: str) -> Dict[str, Any]:
        """
        Evaluate a single survey file.

        For each aspect (outline/content/reference):
        1. Extract texts
        2. Generate embeddings
        3. Query ChromaDB for top-N similar Human entries (or max similarity if use_ams=True)
        4. Compute mean similarity (or F1 for outline in AMS mode)
        """
        start = time.time()
        self.logger.debug(f"Evaluating {file_path.name}")

        survey = self._load_survey(file_path)
        scores: Dict[str, Any] = {}

        # Outline
        if self.config.eval_outline:
            if self.config.use_ams:
                scores["outline"] = self._compute_aspect_f1(survey, category, "outline")
            else:
                scores["outline"] = self._compute_similarity(
                    survey, category, "outline", self.config.outline_top_n
                )
        else:
            scores["outline"] = None

        # Content
        if self.config.eval_content:
            if self.config.use_ams and self.config.use_bidirectional_for_all:
                scores["content"] = self._compute_aspect_f1(survey, category, "content")
            elif self.config.use_ams:
                scores["content"] = self._compute_ams_similarity(survey, category, "content")
            else:
                scores["content"] = self._compute_similarity(
                    survey, category, "content", self.config.content_top_n
                )
        else:
            scores["content"] = None

        # Reference
        if self.config.eval_reference:
            if self.config.use_ams and self.config.use_bidirectional_for_all:
                scores["reference"] = self._compute_aspect_f1(survey, category, "reference")
            elif self.config.use_ams:
                scores["reference"] = self._compute_ams_similarity(survey, category, "reference")
            else:
                scores["reference"] = self._compute_similarity(
                    survey, category, "reference", self.config.reference_top_n
                )
        else:
            scores["reference"] = None

        duration = round(time.time() - start, 2)
        return {
            "file": str(file_path),
            "category": category,
            "scores": scores,
            "duration_seconds": duration,
        }

    def _compute_similarity(
        self, survey: SurveyData, category: str, aspect: str, top_n: int
    ) -> Optional[float]:
        """
        Compute similarity score for a given aspect.

        Args:
            survey: Survey to evaluate
            category: Category name
            aspect: "outline", "content", or "reference"
            top_n: Number of top similar entries to average

        Returns:
            Mean similarity score (0-1) or None if error
        """
        # Extract texts
        if aspect == "outline":
            texts = extract_outline_texts(survey)
        elif aspect == "content":
            texts = extract_content_texts(survey)
        elif aspect == "reference":
            texts = extract_reference_texts(survey)
        else:
            raise ValueError(f"Unknown aspect: {aspect}")

        if not texts:
            self.logger.warning(f"No {aspect} texts found for {category}")
            return None
        
        self.logger.debug(f"Extracted {len(texts)} {aspect} texts")

        # Get Human collection
        coll_name = collection_name_for(category, aspect, "Human")
        try:
            collection = self.chroma_client.get_collection(coll_name)
            count = collection.count()
            if count == 0:
                self.logger.error(
                    f"Collection {coll_name} exists but is empty! "
                    f"Did you run --build-index for {category}?"
                )
                return None
            self.logger.debug(f"Using collection {coll_name} with {count} entries")
        except Exception as exc:
            self.logger.error(f"Collection not found: {coll_name}: {exc}")
            return None

        # Generate embeddings
        try:
            embeddings = self.embedding_client.embed_texts_batch(texts)
        except Exception as exc:
            self.logger.error(f"Embedding generation failed: {exc}")
            return None

        # Query for each entry and collect top scores
        all_scores = []
        for embedding in embeddings:
            try:
                results = collection.query(
                    query_embeddings=[embedding],
                    n_results=1,  # Get most similar
                    include=["distances"],
                )
                if results["distances"] and results["distances"][0]:
                    distance = results["distances"][0][0]
                    # Convert distance to similarity
                    # Use max(0, ...) to ensure non-negative similarity
                    similarity = max(0.0, 1.0 - distance)
                    all_scores.append(similarity)
            except Exception as exc:
                self.logger.error(f"Query failed: {exc}")

        if not all_scores:
            self.logger.warning(
                f"No valid similarity scores for {aspect} in {category}. "
                f"Attempted {len(embeddings)} queries but all failed."
            )
            return None

        # Sort and take top N
        all_scores.sort(reverse=True)
        top_scores = all_scores[:top_n]

        # Return mean
        return sum(top_scores) / len(top_scores)

    def _compute_ams_similarity(
        self, survey: SurveyData, category: str, aspect: str
    ) -> Optional[float]:
        """
        Compute Average Maximum Similarity (AMS) for a given aspect.
        
        For each generated entry, find the maximum similarity with any Human entry,
        then compute the average of these maximum similarities.
        
        Args:
            survey: Survey to evaluate
            category: Category name
            aspect: "content" or "reference"
            
        Returns:
            Average of maximum similarities (0-1) or None if error
        """
        # Extract texts
        if aspect == "content":
            texts = extract_content_texts(survey)
        elif aspect == "reference":
            texts = extract_reference_texts(survey)
        else:
            raise ValueError(f"AMS only supports content/reference, got: {aspect}")

        if not texts:
            self.logger.warning(f"No {aspect} texts found for {category}")
            return None
        
        self.logger.debug(f"Computing AMS for {len(texts)} {aspect} texts")

        # Get Human collection
        coll_name = collection_name_for(category, aspect, "Human")
        try:
            collection = self.chroma_client.get_collection(coll_name)
            count = collection.count()
            if count == 0:
                self.logger.error(f"Collection {coll_name} is empty!")
                return None
            self.logger.debug(f"Using collection {coll_name} with {count} entries")
        except Exception as exc:
            self.logger.error(f"Collection not found: {coll_name}: {exc}")
            return None

        # Generate embeddings for all generated texts
        try:
            embeddings = self.embedding_client.embed_texts_batch(texts)
        except Exception as exc:
            self.logger.error(f"Embedding generation failed: {exc}")
            return None

        threshold = self._get_threshold_for_aspect(aspect)

        # For each generated entry, find maximum similarity with Human entries
        max_similarities = []
        for embedding in embeddings:
            try:
                # Query for the most similar Human entry
                results = collection.query(
                    query_embeddings=[embedding],
                    n_results=1,  # Get only the most similar
                    include=["distances"],
                )
                if results["distances"] and results["distances"][0]:
                    distance = results["distances"][0][0]
                    # Convert distance to similarity
                    # Use max(0, ...) to ensure non-negative similarity
                    similarity = max(0.0, 1.0 - distance)
                    if self.config.use_thresholded_ams and similarity < threshold:
                        similarity = 0.0
                    max_similarities.append(similarity)
            except Exception as exc:
                self.logger.error(f"Query failed: {exc}")

        if not max_similarities:
            self.logger.warning(f"No valid similarity scores for {aspect} in {category}")
            return None

        # Return average of maximum similarities
        ams = sum(max_similarities) / len(max_similarities)
        self.logger.debug(f"AMS for {aspect}: {ams:.4f} (from {len(max_similarities)} entries)")
        return ams

    def _compute_aspect_f1(
        self, survey: SurveyData, category: str, aspect: str
    ) -> Optional[Dict[str, float]]:
        """
        Compute F1 score for an aspect using bidirectional maximum similarity.
        
        - Precision (G→H): For each generated entry, find max similarity with Human entries
        - Recall (H→G): For each Human entry, find max similarity with generated entries
        - F1: Harmonic mean of precision and recall
        
        Args:
            survey: Survey to evaluate
            category: Category name
            aspect: "outline", "content", or "reference"
            
        Returns:
            Dict with precision, recall, and f1 scores, or None if error.
            When use_thresholded_ams=True, includes thresholded_ams as well.
        """
        # Extract generated texts based on aspect
        if aspect == "outline":
            generated_texts = extract_outline_texts(survey)
        elif aspect == "content":
            generated_texts = extract_content_texts(survey)
        elif aspect == "reference":
            generated_texts = extract_reference_texts(survey)
        else:
            raise ValueError(f"Unknown aspect: {aspect}")
            
        if not generated_texts:
            self.logger.warning(f"No {aspect} texts found in generated survey")
            return None
        
        self.logger.debug(f"Computing {aspect} F1 for {len(generated_texts)} generated entries")

        # Get Human collection
        coll_name = collection_name_for(category, aspect, "Human")
        try:
            collection = self.chroma_client.get_collection(coll_name)
            count = collection.count()
            if count == 0:
                self.logger.error(f"Collection {coll_name} is empty!")
                return None
            self.logger.debug(f"Using collection {coll_name} with {count} entries")
        except Exception as exc:
            self.logger.error(f"Collection not found: {coll_name}: {exc}")
            return None

        # Generate embeddings for generated texts
        try:
            generated_embeddings = self.embedding_client.embed_texts_batch(generated_texts)
        except Exception as exc:
            self.logger.error(f"Embedding generation failed: {exc}")
            return None

        # Compute Precision (G→H): For each generated entry, find max similarity with Human
        precision_scores = []
        for embedding in generated_embeddings:
            try:
                results = collection.query(
                    query_embeddings=[embedding],
                    n_results=1,
                    include=["distances"],
                )
                if results["distances"] and results["distances"][0]:
                    distance = results["distances"][0][0]
                    # Convert distance to similarity
                    # For cosine distance: similarity = 1 - distance (range [0, 1])
                    # For L2 distance on normalized vectors: similarity = 1 - distance/2 (range [0, 1])
                    # We use max(0, ...) to handle edge cases
                    similarity = max(0.0, 1.0 - distance)
                    precision_scores.append(similarity)
            except Exception as exc:
                self.logger.error(f"Query failed: {exc}")

        if not precision_scores:
            self.logger.warning(f"No valid precision scores for {aspect} in {category}")
            return None
        
        threshold = self._get_threshold_for_aspect(aspect)
        if self.config.use_threshold:
            precision_hits = sum(1 for score in precision_scores if score >= threshold)
            precision = precision_hits / len(precision_scores)
        else:
            precision = sum(precision_scores) / len(precision_scores)
        
        # Compute Recall (H→G): For each Human entry, find max similarity with generated
        # We need to get all Human texts and their embeddings
        try:
            # Get all documents from the collection
            all_human_data = collection.get(include=["embeddings", "documents"])
            human_embeddings = all_human_data.get("embeddings", [])
            
            if not human_embeddings:
                self.logger.error(f"No embeddings found in Human collection {coll_name}")
                return None
                
        except Exception as exc:
            self.logger.error(f"Failed to retrieve Human embeddings: {exc}")
            return None

        # For each Human embedding, find max similarity with generated embeddings
        recall_scores = []
        for human_embedding in human_embeddings:
            try:
                # Create a temporary collection with generated embeddings to query against
                # Or compute similarity directly
                max_sim = 0.0
                for gen_embedding in generated_embeddings:
                    # Compute cosine similarity manually
                    dot_product = sum(h * g for h, g in zip(human_embedding, gen_embedding))
                    norm_h = sum(h * h for h in human_embedding) ** 0.5
                    norm_g = sum(g * g for g in gen_embedding) ** 0.5
                    
                    if norm_h > 0 and norm_g > 0:
                        similarity = dot_product / (norm_h * norm_g)
                        similarity = max(0.0, similarity)
                        max_sim = max(max_sim, similarity)
                
                recall_scores.append(max_sim)
            except Exception as exc:
                self.logger.error(f"Failed to compute recall similarity: {exc}")

        if not recall_scores:
            self.logger.warning(f"No valid recall scores for {aspect} in {category}")
            return None

        if self.config.use_threshold:
            recall_hits = sum(1 for score in recall_scores if score >= threshold)
            recall = recall_hits / len(recall_scores)
        else:
            recall = sum(recall_scores) / len(recall_scores)
        
        # Compute F1 score
        if precision + recall > 0:
            f1 = 2 * (precision * recall) / (precision + recall)
        else:
            f1 = 0.0
        
        self.logger.debug(
            f"{aspect.capitalize()} F1 scores - Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}"
        )
        
        result: Dict[str, float] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }
        
        if self.config.use_thresholded_ams:
            thresholded_scores = [
                score if score >= threshold else 0.0 for score in precision_scores
            ]
            result["thresholded_ams"] = (
                sum(thresholded_scores) / len(thresholded_scores)
                if thresholded_scores
                else 0.0
            )
        
        return result

    def _get_threshold_for_aspect(self, aspect: str) -> float:
        if aspect == "outline":
            return self.config.outline_threshold
        if aspect == "content":
            return self.config.content_threshold
        if aspect == "reference":
            return self.config.reference_threshold
        raise ValueError(f"Unknown aspect: {aspect}")

    def _compute_averages(self, files: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Compute average scores across files."""
        totals = {"outline": 0.0, "content": 0.0, "reference": 0.0}
        counts = {"outline": 0, "content": 0, "reference": 0}
        
        # For F1 scores (when use_ams=True, and use_bidirectional_for_all=True for content/reference)
        f1_totals = {
            "outline": {"precision": 0.0, "recall": 0.0, "f1": 0.0},
            "content": {"precision": 0.0, "recall": 0.0, "f1": 0.0},
            "reference": {"precision": 0.0, "recall": 0.0, "f1": 0.0},
        }
        f1_counts = {"outline": 0, "content": 0, "reference": 0}
        thresholded_ams_totals = {"outline": 0.0, "content": 0.0, "reference": 0.0}
        thresholded_ams_counts = {"outline": 0, "content": 0, "reference": 0}

        for entry in files:
            scores = entry.get("scores", {})
            for aspect in totals:
                score = scores.get(aspect)
                if isinstance(score, dict):
                    # Handle F1 scores (outline/content/reference when use_bidirectional_for_all=True)
                    if "f1" in score and isinstance(score["f1"], (int, float)):
                        f1_totals[aspect]["precision"] += score.get("precision", 0.0)
                        f1_totals[aspect]["recall"] += score.get("recall", 0.0)
                        f1_totals[aspect]["f1"] += score["f1"]
                        f1_counts[aspect] += 1
                    if "thresholded_ams" in score and isinstance(
                        score["thresholded_ams"], (int, float)
                    ):
                        thresholded_ams_totals[aspect] += score["thresholded_ams"]
                        thresholded_ams_counts[aspect] += 1
                elif isinstance(score, (int, float)):
                    totals[aspect] += score
                    counts[aspect] += 1

        result = {}
        for aspect in totals:
            if f1_counts[aspect] > 0:
                # Return averaged F1 scores
                result[aspect] = {
                    "precision": f1_totals[aspect]["precision"] / f1_counts[aspect],
                    "recall": f1_totals[aspect]["recall"] / f1_counts[aspect],
                    "f1": f1_totals[aspect]["f1"] / f1_counts[aspect],
                }
                if thresholded_ams_counts[aspect] > 0:
                    result[aspect]["thresholded_ams"] = (
                        thresholded_ams_totals[aspect] / thresholded_ams_counts[aspect]
                    )
            else:
                result[aspect] = (totals[aspect] / counts[aspect] if counts[aspect] else None)
        
        return result

    def _load_survey(self, json_path: Path) -> SurveyData:
        """Load survey from JSON."""
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return SurveyData.from_dict(data)

    def _get_systems(self) -> List[str]:
        """Get all available systems."""
        processed_dir = Path(self.config.processed_dir)
        return [d.name for d in processed_dir.iterdir() if d.is_dir()]

    def _get_categories(self, system: str) -> List[str]:
        """Get all categories for a system."""
        system_dir = Path(self.config.processed_dir) / system
        return [d.name for d in system_dir.iterdir() if d.is_dir()]


# ----------------------------- CLI ----------------------------- #


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Quantitative evaluation using embedding similarity"
    )
    parser.add_argument("--config", help="Path to config JSON")
    parser.add_argument("--save-config", help="Save default config and exit")
    parser.add_argument(
        "--build-index",
        action="store_true",
        help="Build Human index before evaluation",
    )
    parser.add_argument("--system", action="append", help="Systems to evaluate")
    parser.add_argument("--category", action="append", help="Categories to evaluate")
    parser.add_argument("--model", help="Embedding model name")
    parser.add_argument("--resume-from", help="Resume from previous evaluation")
    parser.add_argument(
        "--use-ams",
        action="store_true",
        help="Use Average Maximum Similarity mode. "
        "For content/reference: average of max similarity per entry (unidirectional). "
        "For outline: F1 score with Precision (G→H) and Recall (H→G). "
        "top_n parameters are ignored in this mode.",
    )
    parser.add_argument(
        "--use-bidirectional-for-all",
        dest="use_bidirectional_for_all",
        action="store_true",
        help="When used with --use-ams, compute bidirectional F1 (precision/recall/f1) "
        "for all aspects (outline/content/reference) instead of just outline. "
        "Without this flag, only outline computes F1, content/reference use unidirectional AMS.",
    )
    parser.add_argument(
        "--use-threshold",
        action="store_true",
        help="When used with AMS F1 scoring, count a match only if max similarity "
        "meets the configured threshold for each aspect.",
    )
    parser.add_argument(
        "--use-thresholded-ams",
        action="store_true",
        help="When used with AMS (content/reference), set max similarities below the "
        "aspect threshold to 0 before averaging.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Save default config if requested
    if args.save_config:
        cfg = QuantitativeEvalConfig()
        cfg.to_json(args.save_config)
        print(f"Default config saved to {args.save_config}")
        return

    # Load config
    config = QuantitativeEvalConfig()
    if args.config:
        config = QuantitativeEvalConfig.from_json(args.config)

    # Override with CLI args
    if args.system:
        config.systems = args.system
    if args.category:
        config.categories = args.category
    if args.model:
        config.embedding_model = args.model
    if args.resume_from:
        config.resume_from = args.resume_from
    if args.use_ams:
        config.use_ams = True
    if args.use_bidirectional_for_all:
        config.use_bidirectional_for_all = True
    if args.use_threshold:
        config.use_threshold = True
    if args.use_thresholded_ams:
        config.use_thresholded_ams = True

    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    
    # Disable verbose HTTP logs from httpx and openai
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)

    # Initialize embedding client
    embedding_model = config.embedding_model or os.environ.get("MODEL")
    if not embedding_model:
        raise ValueError("No embedding model specified (use --model or MODEL env var)")

    embedding_client = EmbeddingClient(
        model=embedding_model,
        api_key=config.embedding_api_key,
        api_base=config.embedding_api_base,
    )

    # Build Human index if requested
    if args.build_index:
        logging.info("Building Human index...")
        index_builder = HumanIndexBuilder(config, embedding_client)
        index_builder.build_indices()
        logging.info("Index building complete")

    # Run evaluation
    logging.info("Starting evaluation...")
    evaluator = QuantitativeEvaluator(config, embedding_client)
    summary = evaluator.evaluate()
    
    print("\n" + "=" * 60)
    print("Evaluation Summary")
    print("=" * 60)
    print(json.dumps(summary.get("by_system", {}), indent=2))


if __name__ == "__main__":
    main()
