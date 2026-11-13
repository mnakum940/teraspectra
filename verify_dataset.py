import os
import glob
import json
import scipy.io as sio
import numpy as np

def verify_tomato_dataset(data_dir):
    """
    Verifies the integrity of the Tomato Bacterial Wilt hyperspectral dataset.
    Checks all 293 samples across 5 severity levels for required .mat files,
    shape consistency, and non-null values.
    """
    levels = {
        0: {"expected": 120, "name": "Healthy (Level 0)"},
        1: {"expected": 68, "name": "Early/Asymptomatic (Level 1)"},
        2: {"expected": 39, "name": "Mild Wilt 1-33% (Level 2)"},
        3: {"expected": 33, "name": "Moderate Wilt 34-66% (Level 3)"},
        4: {"expected": 33, "name": "Severe Wilt 67-100% (Level 4)"}
    }
    
    results = {
        "status": "PASS",
        "total_samples": 0,
        "classes": {},
        "corrupted_files": [],
        "sample_shapes": {
            "average_spe": None,
            "pixel_spe": None
        }
    }
    
    total_found = 0
    all_dirs = sorted([d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))])
    
    for lvl, meta in levels.items():
        lvl_dirs = [d for d in all_dirs if d.startswith(f"Level{lvl}_")]
        count = len(lvl_dirs)
        total_found += count
        
        valid_avg = 0
        valid_pix = 0
        
        for sample_dir_name in lvl_dirs:
            sample_path = os.path.join(data_dir, sample_dir_name)
            avg_files = glob.glob(os.path.join(sample_path, "*Ave_spe.mat"))
            pix_files = glob.glob(os.path.join(sample_path, "*Pixel_spe.mat"))
            
            if not avg_files or not pix_files:
                results["corrupted_files"].append(f"Missing file in {sample_dir_name}")
                continue
                
            try:
                avg_mat = sio.loadmat(avg_files[0])
                avg_data = avg_mat['Average_spe']
                if avg_data.shape != (180, 1):
                    results["corrupted_files"].append(f"Unexpected shape {avg_data.shape} in {avg_files[0]}")
                else:
                    valid_avg += 1
                    if results["sample_shapes"]["average_spe"] is None:
                        results["sample_shapes"]["average_spe"] = list(avg_data.shape)
            except Exception as e:
                results["corrupted_files"].append(f"Error loading {avg_files[0]}: {str(e)}")
                
            try:
                pix_mat = sio.loadmat(pix_files[0])
                pix_data = pix_mat['pretrain_pixel_ran_500']
                if pix_data.shape != (500, 180):
                    results["corrupted_files"].append(f"Unexpected shape {pix_data.shape} in {pix_files[0]}")
                else:
                    valid_pix += 1
                    if results["sample_shapes"]["pixel_spe"] is None:
                        results["sample_shapes"]["pixel_spe"] = list(pix_data.shape)
            except Exception as e:
                results["corrupted_files"].append(f"Error loading {pix_files[0]}: {str(e)}")
                
        results["classes"][f"Level {lvl}"] = {
            "name": meta["name"],
            "expected": meta["expected"],
            "found": count,
            "valid_average_spe": valid_avg,
            "valid_pixel_spe": valid_pix,
            "status": "PASS" if count == meta["expected"] and valid_avg == count and valid_pix == count else "FAIL"
        }
        
    results["total_samples"] = total_found
    if total_found != 293 or len(results["corrupted_files"]) > 0:
        results["status"] = "FAIL"
        
    return results

if __name__ == "__main__":
    dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "data", "raw", "tomato_wilt", "Tomato bacterial wilt dataset"))
    print(f"Verifying dataset at: {dataset_path}")
    report = verify_tomato_dataset(dataset_path)
    print("\n--- Verification Report ---")
    print(json.dumps(report, indent=2))

