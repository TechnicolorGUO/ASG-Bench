"""
Analysis utilities for evaluation results.

This module provides functions to read evaluation summary JSON files
and aggregate results by different dimensions (system, category, etc.),
then export to CSV for further analysis.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional
from collections import defaultdict


logger = logging.getLogger(__name__)


class EvaluationResultsAnalyzer:
    """Analyzer for evaluation summary JSON files."""

    def __init__(self, results_path: str):
        """
        Initialize analyzer with evaluation results JSON.
        
        Args:
            results_path: Path to evaluation_summary JSON file
        """
        self.results_path = Path(results_path)
        self.data = self._load_results()
        
    def _load_results(self) -> Dict[str, Any]:
        """Load evaluation results from JSON file."""
        if not self.results_path.exists():
            raise FileNotFoundError(f"Results file not found: {self.results_path}")
        
        with open(self.results_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        logger.info(f"Loaded results from {self.results_path}")
        return data
    
    def aggregate_by_system(self) -> List[Dict[str, Any]]:
        """
        Aggregate scores by system (averaging across all categories).
        
        Returns:
            List of dicts with system-level averages:
            [{"system": "Gemini", "outline": 3.5, "content": 4.0, "reference": 3.8, "count": 100}, ...]
        """
        results = []
        by_system = self.data.get("by_system", {})
        
        for system, categories in by_system.items():
            scores = defaultdict(list)
            total_files = 0
            
            for category, cat_data in categories.items():
                files = cat_data.get("files", [])
                total_files += len(files)
                
                for file_entry in files:
                    file_scores = file_entry.get("scores", {})
                    for aspect in ["outline", "content", "reference"]:
                        score = file_scores.get(aspect, {}).get("score")
                        if isinstance(score, (int, float)):
                            scores[aspect].append(score)
            
            result = {"system": system, "count": total_files}
            for aspect in ["outline", "content", "reference"]:
                if scores[aspect]:
                    result[aspect] = round(sum(scores[aspect]) / len(scores[aspect]), 3)
                else:
                    result[aspect] = None
            
            # Calculate overall average
            valid_scores = [v for k, v in result.items() 
                          if k in ["outline", "content", "reference"] and v is not None]
            if valid_scores:
                result["average"] = round(sum(valid_scores) / len(valid_scores), 3)
            else:
                result["average"] = None
            
            results.append(result)
        
        return sorted(results, key=lambda x: x["system"])
    
    def aggregate_by_category(self) -> List[Dict[str, Any]]:
        """
        Aggregate scores by category/domain (averaging across all systems).
        
        Returns:
            List of dicts with category-level averages:
            [{"category": "Biology", "outline": 3.2, "content": 3.9, "reference": 3.5, "count": 50}, ...]
        """
        category_scores = defaultdict(lambda: defaultdict(list))
        category_counts = defaultdict(int)
        
        by_system = self.data.get("by_system", {})
        
        for system, categories in by_system.items():
            for category, cat_data in categories.items():
                files = cat_data.get("files", [])
                category_counts[category] += len(files)
                
                for file_entry in files:
                    file_scores = file_entry.get("scores", {})
                    for aspect in ["outline", "content", "reference"]:
                        score = file_scores.get(aspect, {}).get("score")
                        if isinstance(score, (int, float)):
                            category_scores[category][aspect].append(score)
        
        results = []
        for category in sorted(category_scores.keys()):
            result = {"category": category, "count": category_counts[category]}
            
            for aspect in ["outline", "content", "reference"]:
                if category_scores[category][aspect]:
                    scores = category_scores[category][aspect]
                    result[aspect] = round(sum(scores) / len(scores), 3)
                else:
                    result[aspect] = None
            
            # Calculate overall average
            valid_scores = [v for k, v in result.items() 
                          if k in ["outline", "content", "reference"] and v is not None]
            if valid_scores:
                result["average"] = round(sum(valid_scores) / len(valid_scores), 3)
            else:
                result["average"] = None
            
            results.append(result)
        
        return results
    
    def aggregate_by_system_category(self) -> List[Dict[str, Any]]:
        """
        Aggregate scores by system-category combination.
        
        Returns:
            List of dicts with system+category averages:
            [{"system": "Gemini", "category": "Biology", "outline": 3.5, ...}, ...]
        """
        results = []
        by_system = self.data.get("by_system", {})
        
        for system, categories in by_system.items():
            for category, cat_data in categories.items():
                files = cat_data.get("files", [])
                scores = defaultdict(list)
                
                for file_entry in files:
                    file_scores = file_entry.get("scores", {})
                    for aspect in ["outline", "content", "reference"]:
                        score = file_scores.get(aspect, {}).get("score")
                        if isinstance(score, (int, float)):
                            scores[aspect].append(score)
                
                result = {
                    "system": system,
                    "category": category,
                    "count": len(files)
                }
                
                for aspect in ["outline", "content", "reference"]:
                    if scores[aspect]:
                        result[aspect] = round(sum(scores[aspect]) / len(scores[aspect]), 3)
                    else:
                        result[aspect] = None
                
                # Calculate overall average
                valid_scores = [v for k, v in result.items() 
                              if k in ["outline", "content", "reference"] and v is not None]
                if valid_scores:
                    result["average"] = round(sum(valid_scores) / len(valid_scores), 3)
                else:
                    result["average"] = None
                
                results.append(result)
        
        return sorted(results, key=lambda x: (x["system"], x["category"]))
    
    def aggregate_overall(self) -> Dict[str, Any]:
        """
        Aggregate scores across all systems and categories.
        
        Returns:
            Dict with overall averages:
            {"outline": 3.5, "content": 4.0, "reference": 3.8, "count": 1000}
        """
        scores = defaultdict(list)
        total_files = 0
        
        by_system = self.data.get("by_system", {})
        
        for system, categories in by_system.items():
            for category, cat_data in categories.items():
                files = cat_data.get("files", [])
                total_files += len(files)
                
                for file_entry in files:
                    file_scores = file_entry.get("scores", {})
                    for aspect in ["outline", "content", "reference"]:
                        score = file_scores.get(aspect, {}).get("score")
                        if isinstance(score, (int, float)):
                            scores[aspect].append(score)
        
        result = {"count": total_files}
        for aspect in ["outline", "content", "reference"]:
            if scores[aspect]:
                result[aspect] = round(sum(scores[aspect]) / len(scores[aspect]), 3)
            else:
                result[aspect] = None
        
        # Calculate overall average
        valid_scores = [v for k, v in result.items() 
                       if k in ["outline", "content", "reference"] and v is not None]
        if valid_scores:
            result["average"] = round(sum(valid_scores) / len(valid_scores), 3)
        else:
            result["average"] = None
        
        return result
    
    def get_detailed_results(self) -> List[Dict[str, Any]]:
        """
        Get detailed file-level results.
        
        Returns:
            List of dicts with per-file scores:
            [{"system": "Gemini", "category": "Biology", "file": "...", 
              "outline": 3, "content": 4, "reference": 3}, ...]
        """
        results = []
        by_system = self.data.get("by_system", {})
        
        for system, categories in by_system.items():
            for category, cat_data in categories.items():
                files = cat_data.get("files", [])
                
                for file_entry in files:
                    file_scores = file_entry.get("scores", {})
                    result = {
                        "system": system,
                        "category": category,
                        "file": file_entry.get("file", ""),
                    }
                    
                    for aspect in ["outline", "content", "reference"]:
                        score = file_scores.get(aspect, {}).get("score")
                        result[aspect] = score if isinstance(score, (int, float)) else None
                    
                    # Calculate average for this file
                    valid_scores = [v for k, v in result.items() 
                                  if k in ["outline", "content", "reference"] and v is not None]
                    if valid_scores:
                        result["average"] = round(sum(valid_scores) / len(valid_scores), 3)
                    else:
                        result["average"] = None
                    
                    results.append(result)
        
        return results
    
    def export_to_csv(self, data: List[Dict[str, Any]], output_path: str) -> None:
        """
        Export aggregated data to CSV file.
        
        Args:
            data: List of dicts to export
            output_path: Path to output CSV file
        """
        if not data:
            logger.warning("No data to export")
            return
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        fieldnames = list(data[0].keys())
        
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        logger.info(f"Exported {len(data)} rows to {output_path}")
    
    def export_all(self, output_dir: str) -> None:
        """
        Export all aggregation types to separate CSV files.
        
        Args:
            output_dir: Directory to save CSV files
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Export by system
        by_system = self.aggregate_by_system()
        self.export_to_csv(by_system, output_dir / "aggregated_by_system.csv")
        
        # Export by category
        by_category = self.aggregate_by_category()
        self.export_to_csv(by_category, output_dir / "aggregated_by_category.csv")
        
        # Export by system-category
        by_sys_cat = self.aggregate_by_system_category()
        self.export_to_csv(by_sys_cat, output_dir / "aggregated_by_system_category.csv")
        
        # Export overall
        overall = self.aggregate_overall()
        self.export_to_csv([overall], output_dir / "aggregated_overall.csv")
        
        # Export detailed results
        detailed = self.get_detailed_results()
        self.export_to_csv(detailed, output_dir / "detailed_results.csv")
        
        logger.info(f"Exported all aggregations to {output_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze evaluation results and export to CSV."
    )
    parser.add_argument(
        "results_json",
        help="Path to evaluation_summary JSON file"
    )
    parser.add_argument(
        "--output-dir",
        default="results/analysis",
        help="Directory to save CSV files (default: results/analysis)"
    )
    parser.add_argument(
        "--aggregation",
        choices=["system", "category", "system-category", "overall", "detailed", "all"],
        default="all",
        help="Type of aggregation to perform (default: all)"
    )
    parser.add_argument(
        "--output-file",
        help="Specific output CSV file (used with non-'all' aggregation types)"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    
    analyzer = EvaluationResultsAnalyzer(args.results_json)
    
    if args.aggregation == "all":
        analyzer.export_all(args.output_dir)
    else:
        # Determine output file
        if args.output_file:
            output_path = args.output_file
        else:
            output_dir = Path(args.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            
            if args.aggregation == "system":
                output_path = output_dir / "aggregated_by_system.csv"
                data = analyzer.aggregate_by_system()
            elif args.aggregation == "category":
                output_path = output_dir / "aggregated_by_category.csv"
                data = analyzer.aggregate_by_category()
            elif args.aggregation == "system-category":
                output_path = output_dir / "aggregated_by_system_category.csv"
                data = analyzer.aggregate_by_system_category()
            elif args.aggregation == "overall":
                output_path = output_dir / "aggregated_overall.csv"
                data = [analyzer.aggregate_overall()]
            elif args.aggregation == "detailed":
                output_path = output_dir / "detailed_results.csv"
                data = analyzer.get_detailed_results()
            else:
                logger.error(f"Unknown aggregation type: {args.aggregation}")
                return
            
            analyzer.export_to_csv(data, output_path)
    
    print(f"Analysis complete. Results saved to {args.output_dir}")


if __name__ == "__main__":
    main()
