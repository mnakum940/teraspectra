# Changelog — Meet (Day 3)

## [Day 3] - 2024-11-12
### Added
- Developed `HyperspectralDataLoader` capable of parsing sample directory hierarchies and extracting `.mat` matrices into clean NumPy arrays.
- Developed `DataValidator` checking spectral dimensions (180 bands), detecting NaN/Inf anomalies, and verifying biological reflectance bounds.
- Established shared interface contract in `main project/src/data/` for downstream preprocessing (Prince) and ML modeling (Shravani).
- Authored and verified `test_data_loader.py` covering scanning, average spectra extraction, and pixel-level sampling.

