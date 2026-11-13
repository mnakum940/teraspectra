# Data Verification Report — Tomato Bacterial Wilt Dataset
**Author:** Meet (Project Lead & Data Pipeline Lead)  
**Date:** 2024-11-12  
**Dataset:** Tomato Bacterial Wilt Severity Identification  
**Source:** Mendeley Data (DOI: 10.17632/tb4yk4x5nw.1)  

---

## 1. Executive Summary
The primary dataset selected for TerraSpectra has been acquired, extracted, and verified. 100% of the sample directories (293/293) contain uncorrupted, fully structured MATLAB `.mat` files holding both canopy-averaged and pixel-level hyperspectral reflectance data.

---

## 2. Directory Hierarchy and Naming Structure
The dataset is arranged into 293 directories within a single top-level folder:
- **Level 0 (Healthy):** `Level0_001` through `Level0_120` (120 samples, 3-digit zero-padding)
- **Level 1 (Infected, Asymptomatic):** `Level1_01` through `Level1_68` (68 samples, 2-digit zero-padding)
- **Level 2 (Mild Wilt, 1–33%):** `Level2_01` through `Level2_39` (39 samples, 2-digit zero-padding)
- **Level 3 (Moderate Wilt, 34–66%):** `Level3_01` through `Level3_33` (33 samples, 2-digit zero-padding)
- **Level 4 (Severe Wilt, 67–100%):** `Level4_01` through `Level4_33` (33 samples, 2-digit zero-padding)

---

## 3. Matrix Structures & Variable Keys

### A. Average Canopy Spectrum (`*Ave_spe.mat`)
- **Key:** `'Average_spe'`
- **Matrix Dimension:** `(180, 1)` (1D column vector)
- **Data Type:** `float64`
- **Dynamic Range:** Approximately `0.02` to `0.65` (Reflectance ratio)
- **Significance:** Represents the integrated mean spectral signature across the canopy Region of Interest (ROI) for that individual plant specimen.

### B. Pixel-Level Canopy Spectra (`*Pixel_spe.mat`)
- **Key:** `'pretrain_pixel_ran_500'`
- **Matrix Dimension:** `(500, 180)`
- **Data Type:** `float64`
- **Dynamic Range:** `0.01` to `0.98`
- **Significance:** 500 spatial pixels sampled randomly within the plant mask. Provides $293 \times 500 = 146,500$ spectral profiles for deep learning (1D-CNN) and intra-plant heterogeneity modeling.

---

## 4. Class Distribution Summary

| Severity Level | Biological Description | Symptom Threshold | Samples | Sample Share (%) |
|---|---|---|---|---|
| **Level 0** | Healthy / Uninoculated Control | No disease symptoms | 120 | 40.96% |
| **Level 1** | Inoculated / Asymptomatic | 0% visible wilting | 68 | 23.21% |
| **Level 2** | Mild Infection | 1% – 33% wilted foliage | 39 | 13.31% |
| **Level 3** | Moderate Infection | 34% – 66% wilted foliage | 33 | 11.26% |
| **Level 4** | Severe Infection / Necrosis | 67% – 100% wilted foliage | 33 | 11.26% |
| **Total** | — | — | **293** | **100.00%** |

---

## 5. Data Pipeline Recommendation
1. Use **Group-stratified splitting** at the plant folder level. Never mix pixels from the same plant across train and test sets to prevent data leakage.
2. For baseline tabular ML (Logistic Regression, Random Forest, SVM, XGBoost), use the 293 plant-level `Average_spe` vectors ($293 \times 180$).
3. For deep learning (1D-CNN), use the pixel-level matrix ($146,500 \times 180$) with plant ID groups preserved.

