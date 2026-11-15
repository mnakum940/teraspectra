"""
Meet Day 4: Dataset Integrity Audit & Comprehensive EDA
Author: Meet (Project Lead & Data Pipeline Lead)
Description: Generates multi-band descriptive statistics, verifies signal quality,
and exports canonical summary tables.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from data.loader import HyperspectralDataLoader, SEVERITY_MAPPING, get_wavelength_grid
from data.validator import DataValidator

def run_dataset_eda():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "data", "raw", "tomato_wilt", "Tomato bacterial wilt dataset"))
    output_table_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "reports", "tables"))
    os.makedirs(output_table_dir, exist_ok=True)
    
    loader = HyperspectralDataLoader(data_dir)
    X, y, df = loader.load_average_spectra()
    wavelengths = get_wavelength_grid(180)
    
    # Calculate band-wise statistics
    stats_records = []
    for b in range(180):
        band_vals = X[:, b]
        mu = float(np.mean(band_vals))
        sigma = float(np.std(band_vals))
        snr = float(mu / (sigma + 1e-8))
        stats_records.append({
            "band_index": b,
            "wavelength_nm": round(float(wavelengths[b]), 2),
            "mean": round(mu, 4),
            "std": round(sigma, 4),
            "min": round(float(np.min(band_vals)), 4),
            "median": round(float(np.median(band_vals)), 4),
            "max": round(float(np.max(band_vals)), 4),
            "snr_db": round(20 * np.log10(snr), 2)
        })
        
    stats_df = pd.DataFrame(stats_records)
    stats_csv_path = os.path.join(output_table_dir, "band_summary_statistics.csv")
    stats_df.to_csv(stats_csv_path, index=False)
    
    print("=== DATASET INTEGRITY & EDA AUDIT (MEET - DAY 4) ===")
    print(f"Total verified specimens: {len(X)}")
    print(f"Total spectral bands:     {X.shape[1]}")
    print(f"Saved band statistics to: {stats_csv_path}")
    print(f"\nTop 5 Highest SNR Bands (cleanest signal):")
    top_snr = stats_df.sort_values(by="snr_db", ascending=False).head(5)
    print(top_snr[["band_index", "wavelength_nm", "mean", "snr_db"]].to_string(index=False))
    
    return stats_df

if __name__ == "__main__":
    run_dataset_eda()

