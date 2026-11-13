# Test Results — Meet (Day 2)

## Test Execution Details
- **Date**: 2024-11-12
- **Script**: `verify_dataset.py`
- **Target**: `main project/data/raw/tomato_wilt/Tomato bacterial wilt dataset`
- **Result**: ALL TESTS PASSED (100% Integrity)

## Execution Output
```json
{
  "status": "PASS",
  "total_samples": 293,
  "classes": {
    "Level 0": {
      "name": "Healthy (Level 0)",
      "expected": 120,
      "found": 120,
      "valid_average_spe": 120,
      "valid_pixel_spe": 120,
      "status": "PASS"
    },
    "Level 1": {
      "name": "Early/Asymptomatic (Level 1)",
      "expected": 68,
      "found": 68,
      "valid_average_spe": 68,
      "valid_pixel_spe": 68,
      "status": "PASS"
    },
    "Level 2": {
      "name": "Mild Wilt 1-33% (Level 2)",
      "expected": 39,
      "found": 39,
      "valid_average_spe": 39,
      "valid_pixel_spe": 39,
      "status": "PASS"
    },
    "Level 3": {
      "name": "Moderate Wilt 34-66% (Level 3)",
      "expected": 33,
      "found": 33,
      "valid_average_spe": 33,
      "valid_pixel_spe": 33,
      "status": "PASS"
    },
    "Level 4": {
      "name": "Severe Wilt 67-100% (Level 4)",
      "expected": 33,
      "found": 33,
      "valid_average_spe": 33,
      "valid_pixel_spe": 33,
      "status": "PASS"
    }
  },
  "corrupted_files": [],
  "sample_shapes": {
    "average_spe": [180, 1],
    "pixel_spe": [500, 180]
  }
}
```

## Summary Criteria
1. Total plant sample count = 293 (Passed)
2. Average spectrum matrix present in 293/293 samples (Passed)
3. Pixel-level spectrum matrix present in 293/293 samples (Passed)
4. Corrupted or unreadable files = 0 (Passed)
5. Dimension consistency across entire dataset = 100% (Passed)

