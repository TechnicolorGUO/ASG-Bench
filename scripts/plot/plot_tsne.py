import argparse
import json
import os
import sys
from pathlib import Path
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.manifold import TSNE
from dotenv import load_dotenv

# Reuse the embedding call path from eval_quantitative.py
SCRIPT_DIR = Path(__file__).resolve().parents[1]
EVAL_DIR = SCRIPT_DIR / "evaluation"
if str(EVAL_DIR) not in sys.path:
    sys.path.append(str(EVAL_DIR))

from eval_quantitative import EmbeddingClient  # type: ignore

load_dotenv()


def load_topics(csv_path: Path, text_column: str, label_column: str) -> Tuple[List[str], List[str]]:
    df = pd.read_csv(csv_path)
    if text_column not in df.columns:
        raise ValueError(f"Text column '{text_column}' not found in {csv_path}")
    if label_column not in df.columns:
        raise ValueError(f"Label column '{label_column}' not found in {csv_path}")

    texts = df[text_column].astype(str).str.strip()
    labels = df[label_column].astype(str).str.strip()
    mask = texts.notna() & (texts != "")
    texts = texts[mask].tolist()
    labels = labels[mask].tolist()
    return texts, labels


def embed_topics(
    texts: List[str],
    model_name: str,
    embeddings_path: Path,
    meta_path: Path,
    batch_size: int = 32,
    force: bool = False,
) -> np.ndarray:
    if embeddings_path.exists() and meta_path.exists() and not force:
        try:
            embeddings = np.load(embeddings_path)
            if embeddings.shape[0] == len(texts):
                return embeddings
        except Exception:
            pass

    client = EmbeddingClient(
        model=model_name,
        api_key=os.environ.get("API_KEY"),
        api_base=os.environ.get("BASE_URL"),
    )

    all_embeddings: List[List[float]] = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        batch_embeddings = client.embed_texts_batch(batch)
        all_embeddings.extend(batch_embeddings)

    embeddings = np.array(all_embeddings, dtype=np.float32)
    embeddings_path.parent.mkdir(parents=True, exist_ok=True)
    np.save(embeddings_path, embeddings)
    meta = {
        "model": model_name,
        "num_texts": len(texts),
        "embeddings_path": str(embeddings_path),
    }
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return embeddings


def compute_tsne(embeddings: np.ndarray, random_state: int = 42) -> np.ndarray:
    n_samples = embeddings.shape[0]
    if n_samples < 2:
        raise ValueError("Need at least 2 samples to run t-SNE")
    max_perplexity = max(5, (n_samples - 1) // 3)
    perplexity = min(30, max_perplexity)
    tsne = TSNE(n_components=2, random_state=random_state, perplexity=perplexity)
    return tsne.fit_transform(embeddings)


def plot_tsne(
    embeddings_2d: np.ndarray,
    labels: List[str],
    output_path: Path,
    title: str = "Question Topics",
    label_fontsize: int = 11,
    point_size: int = 14,
    padding_ratio: float = 0.04,
) -> None:
    df_plot = pd.DataFrame(
        {
            "x": embeddings_2d[:, 0],
            "y": embeddings_2d[:, 1],
            "label": labels,
        }
    )

    plt.figure(figsize=(8, 8))
    unique_labels = sorted(df_plot["label"].unique())
    palette = sns.color_palette("husl", len(unique_labels))

    sns.scatterplot(
        data=df_plot,
        x="x",
        y="y",
        hue="label",
        palette=palette,
        s=point_size,
        alpha=0.6,
        linewidth=0,
    )

    # Add cluster labels at centroid positions
    for label in unique_labels:
        cluster = df_plot[df_plot["label"] == label]
        x_center = cluster["x"].mean()
        y_center = cluster["y"].mean()
        plt.annotate(
            label,
            (x_center, y_center),
            ha="center",
            va="center",
            fontsize=label_fontsize,
            color="white",
            bbox=dict(boxstyle="round,pad=0.3", fc="gray", ec="none", alpha=0.7),
        )

    plt.title(title)
    plt.legend([], [], frameon=False)
    # Tighter bounds around points
    x_min, x_max = df_plot["x"].min(), df_plot["x"].max()
    y_min, y_max = df_plot["y"].min(), df_plot["y"].max()
    x_pad = (x_max - x_min) * padding_ratio
    y_pad = (y_max - y_min) * padding_ratio
    plt.xlim(x_min - x_pad, x_max + x_pad)
    plt.ylim(y_min - y_pad, y_max + y_pad)
    plt.tight_layout(pad=0.5)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="t-SNE plot for topic embeddings")
    parser.add_argument(
        "--csv",
        default="summary_v14(3).csv",
        help="Input CSV path",
    )
    parser.add_argument(
        "--text-column",
        default="Title",
        help="Column for topic text",
    )
    parser.add_argument(
        "--label-column",
        default="Subject",
        help="Column for label",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("MODEL"),
        help="Embedding model name (or set MODEL env var)",
    )
    parser.add_argument(
        "--embeddings",
        default="results/plots/topic_embeddings.npy",
        help="Path to save embeddings",
    )
    parser.add_argument(
        "--meta",
        default="results/plots/topic_embeddings_meta.json",
        help="Path to save embedding metadata",
    )
    parser.add_argument(
        "--plot",
        default="results/plots/question_topics_tsne.png",
        help="Output plot path",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=32,
        help="Embedding batch size",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Recompute embeddings even if cache exists",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.model:
        raise ValueError("No embedding model specified (use --model or MODEL env var)")

    csv_path = Path(args.csv)
    texts, labels = load_topics(csv_path, args.text_column, args.label_column)
    embeddings = embed_topics(
        texts,
        args.model,
        Path(args.embeddings),
        Path(args.meta),
        batch_size=args.batch_size,
        force=args.force,
    )
    embeddings_2d = compute_tsne(embeddings)
    plot_tsne(embeddings_2d, labels, Path(args.plot))


if __name__ == "__main__":
    main()