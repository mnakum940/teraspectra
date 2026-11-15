# Data Integrity & Signal-to-Noise Ratio (SNR) Report
**Author:** Meet (Project Lead & Data Pipeline Lead)  
**Date:** 2024-11-12  
**Dataset:** Tomato Bacterial Wilt Hyperspectral Dataset (Specim IQ)  

---

## 1. Scope of Audit
A rigorous statistical audit was conducted across all 293 tomato plant specimens ($293 \times 180 = 52,740$ discrete reflectance measurements) to quantify signal stability and identify noise regimes.

---

## 2. Band-Wise Signal-to-Noise Profile
Signal-to-noise ratio was quantified as:
$$\text{SNR}_{\text{dB}} = 20 \log_{10} \left( \frac{\mu_{\lambda}}{\sigma_{\lambda}} \right)$$

### Key Regime Observations:
1. **Red Edge Onset ($690\text{ nm} - 710\text{ nm}$):**
   - Exhibits highest SNR ($>22.3\text{ dB}$).
   - Very tight reflectance clustering in healthy samples coupled with strong dynamic shift in diseased plants.
2. **Visible Pigment Region ($400\text{ nm} - 550\text{ nm}$):**
   - Moderate SNR ($18 - 20\text{ dB}$).
   - High photon absorption yields lower mean reflectance ($\mu \approx 0.07 - 0.11$).
3. **Extreme NIR Taper ($960\text{ nm} - 1000\text{ nm}$):**
   - Lowest SNR regime ($14 - 16\text{ dB}$).
   - Minor atmospheric water vapor interference and silicon detector quantum efficiency attenuation.

---

## 3. Data Integrity Certification
- **Null values:** 0 (100% complete)
- **Extreme outliers ($>3\sigma$):** Handled consistently across all clinical groups
- **Physical plausibility:** All reflectance measurements fall strictly within $[0.046, 0.529]$ range for canopy averages.

