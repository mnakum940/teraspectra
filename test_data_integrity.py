import os
import sys
import pandas as pd

def test_exported_eda():
    table_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "reports", "tables", "band_summary_statistics.csv"))
    assert os.path.exists(table_path), f"Summary statistics table not found at {table_path}"
    df = pd.read_csv(table_path)
    print(f"Verified summary statistics: {len(df)} bands loaded.")
    assert len(df) == 180, f"Expected 180 bands, got {len(df)}"
    assert df["mean"].isnull().sum() == 0, "Null values detected in band means"
    assert df["std"].isnull().sum() == 0, "Null values detected in band stds"
    assert (df["snr_db"] > 0).all(), "Negative SNR detected in spectral bands"
    print("ALL DATA INTEGRITY & STATISTICAL AUDIT TESTS PASSED!")

if __name__ == "__main__":
    test_exported_eda()

