import os
import sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from data.loader import HyperspectralDataLoader
from features.pipeline import CompositeFeaturePipeline

def test_feature_pipeline():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "data", "raw", "tomato_wilt", "Tomato bacterial wilt dataset"))
    loader = HyperspectralDataLoader(data_dir)
    X, y, df = loader.load_average_spectra()
    
    pipeline = CompositeFeaturePipeline(n_pca_components=8)
    feats = pipeline.fit_transform(X)
    
    print(f"Generated representations for {len(X)} samples:")
    for name, mat in feats.items():
        print(f"  {name:<12}: shape {mat.shape}, min={mat.min():.3f}, max={mat.max():.3f}")
        assert mat.shape[0] == 293
        assert np.isnan(mat).sum() == 0, f"NaN in {name}"
        
    assert feats["full_bands"].shape == (293, 180)
    assert feats["pca"].shape == (293, 8)
    assert feats["biomarkers"].shape == (293, 12)
    assert feats["hybrid"].shape == (293, 20)
    
    print("\nALL COMPOSITE FEATURE PIPELINE TESTS PASSED!")

if __name__ == "__main__":
    test_feature_pipeline()

