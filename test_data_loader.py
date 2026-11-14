import os
import sys
import numpy as np

# Ensure path includes main project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from data.loader import HyperspectralDataLoader, SEVERITY_MAPPING, get_wavelength_grid
from data.validator import DataValidator

def test_loader_and_validator():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "data", "raw", "tomato_wilt", "Tomato bacterial wilt dataset"))
    print(f"Testing DataLoader on: {data_dir}")
    
    loader = HyperspectralDataLoader(data_dir)
    df_meta = loader.scan_dataset()
    print(f"Scanned {len(df_meta)} sample folders.")
    assert len(df_meta) == 293, f"Expected 293 samples, got {len(df_meta)}"
    
    X, y, df = loader.load_average_spectra()
    print(f"Loaded feature matrix X: shape {X.shape}, dtype {X.dtype}")
    print(f"Loaded target vector y: shape {y.shape}, classes: {np.unique(y)}")
    
    assert X.shape == (293, 180), f"Expected (293, 180), got {X.shape}"
    assert len(y) == 293, f"Expected 293 labels, got {len(y)}"
    assert set(np.unique(y)) == {0, 1, 2, 3, 4}, f"Unexpected classes: {np.unique(y)}"
    
    # Test validator
    matrix_report = DataValidator.validate_matrix(X, y)
    print("Matrix validation report:")
    for k, v in matrix_report.items():
        print(f"  {k}: {v}")
    assert matrix_report["valid"] is True, f"Validation failed: {matrix_report['issues']}"
    
    # Test pixel loading
    first_sample_id = df.iloc[0]["sample_id"]
    pix_data = loader.load_pixel_spectra(first_sample_id)
    print(f"Loaded pixel spectra for {first_sample_id}: shape {pix_data.shape}")
    assert pix_data.shape == (500, 180), f"Expected (500, 180), got {pix_data.shape}"
    
    print("\nALL LOADER & VALIDATOR UNIT TESTS PASSED!")

if __name__ == "__main__":
    test_loader_and_validator()

