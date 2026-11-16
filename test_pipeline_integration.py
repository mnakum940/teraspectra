import os
import sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from data.loader import HyperspectralDataLoader
from preprocessing.pipeline import SpectralPreprocessingPipeline

def test_pipeline_integration():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "data", "raw", "tomato_wilt", "Tomato bacterial wilt dataset"))
    loader = HyperspectralDataLoader(data_dir)
    X, y, df = loader.load_average_spectra()
    
    # 1. Test SNV + Smoothing mode
    pipe_smooth = SpectralPreprocessingPipeline(mode="snv_smooth")
    X_proc = pipe_smooth.fit_transform(X)
    assert X_proc.shape == (293, 180)
    print("SNV + Smoothing pipeline executed successfully, shape:", X_proc.shape)
    
    # 2. Test SNV + Derivative mode
    pipe_deriv = SpectralPreprocessingPipeline(mode="snv_deriv")
    X_deriv = pipe_deriv.fit_transform(X)
    assert X_deriv.shape == (293, 180)
    print("SNV + Derivative pipeline executed successfully, shape:", X_deriv.shape)
    
    # 3. Test serialization
    test_save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_pipeline.joblib"))
    pipe_smooth.save(test_save_path)
    assert os.path.exists(test_save_path)
    
    # 4. Test deserialization
    loaded_pipe = SpectralPreprocessingPipeline.load(test_save_path)
    X_reloaded = loaded_pipe.transform(X[:5])
    np.testing.assert_allclose(X_reloaded, X_proc[:5])
    print("Pipeline serialization and deserialization verified!")
    
    if os.path.exists(test_save_path):
        os.remove(test_save_path)
        
    print("\nALL PREPROCESSING PIPELINE INTEGRATION TESTS PASSED!")

if __name__ == "__main__":
    test_pipeline_integration()

