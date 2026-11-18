"""
Meet Day 7: Prediction Pipeline Snapshot
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from models.pipeline import DiseasePredictionPipeline

__all__ = ["DiseasePredictionPipeline"]

