"""
Meet Day 6: Feature Pipeline Snapshot
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from features.pipeline import CompositeFeaturePipeline

__all__ = ["CompositeFeaturePipeline"]

