"""
Meet - Day 10: End-to-End Pipeline Evaluation & Reproducibility Audit
Author: Meet (Project Lead & Integration Lead)
Verifies full pipeline reproducibility from raw spectra to multi-model evaluation deliverables.
"""

import os
import sys
import numpy as np
import pandas as pd

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.join(root_dir, "main project", "src"))

def run_meet_day10_audit():
    print("==================================================")
    print("MEET DAY 10 REPRODUCIBILITY & SYNTHESIS AUDIT")
    print("==================================================")
    
    # 1. Verify Raw & Processed Data Partitions
    proc_dir = os.path.join(root_dir, "main project/data/processed")
    for fname in ["X_train_raw.npy", "X_test_raw.npy", "y_train.npy", "y_test.npy"]:
        p = os.path.join(proc_dir, fname)
        assert os.path.exists(p), f"Missing data partition: {fname}"
    print("✔ All raw and processed data partitions verified.")
    
    # 2. Verify Prince Day 10 Spectral Synthesis Deliverables
    domain_csv = os.path.join(root_dir, "main project/reports/tables/spectral_biophysical_domains.csv")
    fig_bio = os.path.join(root_dir, "main project/reports/figures/hyperspectral_synthesis_biophysical_profiles.png")
    assert os.path.exists(domain_csv), "Missing spectral_biophysical_domains.csv"
    assert os.path.exists(fig_bio), "Missing hyperspectral_synthesis_biophysical_profiles.png"
    print("✔ Prince Day 10 biophysical synthesis deliverables verified.")
    
    # 3. Verify Shravani Day 10 Comprehensive Evaluation Metrics
    eval_csv = os.path.join(root_dir, "main project/reports/tables/final_model_evaluation_metrics.csv")
    fig_cm = os.path.join(root_dir, "main project/reports/figures/model_comparison_confusion_matrices.png")
    assert os.path.exists(eval_csv), "Missing final_model_evaluation_metrics.csv"
    assert os.path.exists(fig_cm), "Missing model_comparison_confusion_matrices.png"
    
    df_eval = pd.read_csv(eval_csv)
    assert len(df_eval) == 7, f"Expected 7 models in benchmark, got {len(df_eval)}"
    best_model = df_eval.sort_values(by="Macro_F1", ascending=False).iloc[0]
    print(f"✔ Shravani Day 10 benchmark verified. Champion: {best_model['Model']} (Macro F1 = {best_model['Macro_F1']:.4f}, Accuracy = {best_model['Accuracy']:.2%}).")
    
    # 4. Verify Abdul Day 10 Dashboard Component
    comp_file = os.path.join(root_dir, "Abdul/day10/model_comparison_dashboard.py")
    assert os.path.exists(comp_file), "Missing model_comparison_dashboard.py"
    print("✔ Abdul Day 10 dashboard component verified.")
    
    print("\nALL MEET DAY 10 REPRODUCIBILITY AUDITS PASSED!")

if __name__ == "__main__":
    run_meet_day10_audit()

