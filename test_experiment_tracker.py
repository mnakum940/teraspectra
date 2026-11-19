import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from utils.experiment_tracker import ExperimentTracker

def test_tracker():
    eval_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "models", "evaluation"))
    tracker = ExperimentTracker(eval_dir)
    
    # Log baseline Random Forest
    r1 = tracker.log_run(
        model_name="Random Forest Baseline",
        feature_space="20-D Hybrid",
        hyperparameters={"n_estimators": 150, "max_depth": 8},
        metrics={"accuracy": 0.8305, "macro_f1": 0.8510, "weighted_f1": 0.8250, "balanced_accuracy": 0.8643}
    )
    
    # Log tuned SVM
    r2 = tracker.log_run(
        model_name="SVM Optimized",
        feature_space="20-D Hybrid",
        hyperparameters={"C": 5.0, "gamma": "auto"},
        metrics={"accuracy": 0.7627, "macro_f1": 0.7514, "weighted_f1": 0.7480, "balanced_accuracy": 0.7607}
    )
    
    # Log tuned RF
    r3 = tracker.log_run(
        model_name="Random Forest Optimized",
        feature_space="20-D Hybrid",
        hyperparameters={"n_estimators": 200, "max_depth": 6, "min_samples_split": 3},
        metrics={"accuracy": 0.7966, "macro_f1": 0.8167, "weighted_f1": 0.8010, "balanced_accuracy": 0.8274}
    )
    
    df_lb = tracker.get_leaderboard()
    print("Leaderboard top rows:")
    print(df_lb[["model_name", "accuracy", "macro_f1", "balanced_accuracy"]].to_string(index=False))
    
    assert len(df_lb) >= 3
    assert df_lb.iloc[0]["macro_f1"] >= df_lb.iloc[1]["macro_f1"], "Leaderboard is not correctly sorted descending"
    print("\nALL EXPERIMENT TRACKER TESTS PASSED!")

if __name__ == "__main__":
    test_tracker()

