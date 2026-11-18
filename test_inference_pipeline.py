import os
import sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from data.loader import HyperspectralDataLoader
from features.pipeline import CompositeFeaturePipeline
from models.random_forest import BaselineRandomForest
from models.pipeline import DiseasePredictionPipeline

def test_prediction_pipeline():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "data", "raw", "tomato_wilt", "Tomato bacterial wilt dataset"))
    loader = HyperspectralDataLoader(data_dir)
    X, y, df = loader.load_average_spectra()
    
    # Fit feature pipeline across dataset
    feat_pipe = CompositeFeaturePipeline(n_pca_components=8)
    feat_pipe.fit(X)
    
    # Load trained Random Forest baseline
    rf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "models", "trained", "random_forest_baseline.joblib"))
    rf = BaselineRandomForest.load(rf_path)
    
    pred_pipe = DiseasePredictionPipeline(feature_pipeline=feat_pipe, model=rf)
    
    # Test on a healthy sample
    h_spe = X[0] # Level 0
    res_h = pred_pipe.predict_spectrum(h_spe)
    print("Healthy prediction result:")
    print(f"  Predicted Level: {res_h['predicted_level']} ({res_h['severity_label']}), Confidence: {res_h['confidence']*100:.1f}%")
    assert res_h["predicted_level"] == 0
    assert res_h["confidence"] > 0.50
    assert len(res_h["class_probabilities"]) == 5
    
    # Test on a severe sample
    s_idx = np.where(y == 4)[0][0]
    s_spe = X[s_idx]
    res_s = pred_pipe.predict_spectrum(s_spe)
    print("Severe wilt prediction result:")
    print(f"  Predicted Level: {res_s['predicted_level']} ({res_s['severity_label']}), Confidence: {res_s['confidence']*100:.1f}%")
    assert res_s["predicted_level"] == 4
    
    print("\nALL PREDICTION PIPELINE INTEGRATION TESTS PASSED!")

if __name__ == "__main__":
    test_prediction_pipeline()
