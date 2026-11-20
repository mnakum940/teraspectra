"""
Meet - Day 9: Architecture Review and Model Pipeline Verification.
Verifies integration of classical ML and 1D-CNN pipelines into unified framework.
"""

import os
import sys
import numpy as np

# Ensure project root is accessible
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.join(root_dir, "main project", "src"))

from models.split_manager import DatasetSplitManager
from models.pipeline import DiseasePredictionPipeline
from models.cnn_model import Spectral1DCNN, PyTorch1DCNNClassifier
from features.pipeline import CompositeFeaturePipeline

def run_meet_day9_tests():
    print("==================================================")
    print("MEET DAY 9 INTEGRATION & ARCHITECTURE AUDIT")
    print("==================================================")
    
    # 1. Verify Processed Data Existence
    proc_dir = os.path.join(root_dir, "main project/data/processed")
    x_train_path = os.path.join(proc_dir, "X_train_processed.npy")
    y_train_path = os.path.join(proc_dir, "y_train.npy")
    x_test_path = os.path.join(proc_dir, "X_test_processed.npy")
    y_test_path = os.path.join(proc_dir, "y_test.npy")
    
    assert os.path.exists(x_train_path), "X_train_processed missing"
    assert os.path.exists(y_train_path), "y_train missing"
    assert os.path.exists(x_test_path), "X_test_processed missing"
    assert os.path.exists(y_test_path), "y_test missing"
    print("✔ Processed data arrays verified.")
    
    # 2. Verify Wavelength Importance Artifacts (Prince Day 9)
    fig_path = os.path.join(root_dir, "main project/reports/figures/wavelength_importance_profile.png")
    csv_path = os.path.join(root_dir, "main project/reports/tables/top_wavelength_importance.csv")
    assert os.path.exists(fig_path), "Wavelength importance figure missing"
    assert os.path.exists(csv_path), "Top wavelength importance CSV missing"
    print("✔ Prince Day 9 wavelength importance deliverables verified.")
    
    # 3. Verify 1D-CNN Artifacts (Shravani Day 9)
    model_pt = os.path.join(root_dir, "main project/models/trained/spectral_1d_cnn.pt")
    history_csv = os.path.join(root_dir, "main project/models/evaluation/cnn_training_history.csv")
    assert os.path.exists(model_pt), "1D-CNN weights missing"
    assert os.path.exists(history_csv), "1D-CNN training history CSV missing"
    print("✔ Shravani Day 9 deep learning deliverables verified.")
    
    # 4. Verify End-to-End Prediction Interface
    import joblib
    feat_pipe = joblib.load(os.path.join(root_dir, "main project/models/feature_pipeline.joblib"))
    rf_model = joblib.load(os.path.join(root_dir, "main project/models/trained/random_forest_optimized.joblib"))
    pipeline = DiseasePredictionPipeline(feat_pipe, rf_model)
    dummy_spectrum = np.random.uniform(0.1, 0.8, (180,))
    res = pipeline.predict_spectrum(dummy_spectrum)
    assert "predicted_level" in res, "Prediction output missing predicted_level"
    assert "class_probabilities" in res, "Prediction output missing class_probabilities"
    print(f"✔ Real-time single-spectrum inference verified (Predicted: Level {res['predicted_level']}).")
    
    print("\nALL MEET DAY 9 ARCHITECTURAL TESTS PASSED!")

if __name__ == "__main__":
    run_meet_day9_tests()
