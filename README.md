# AutoWorth — Car Price Predictor

A Flask app that estimates a used car's price from its make, model, year, fuel type, and kilometres driven. The dashboard summarizes the included listings, and separate pages provide the estimator and project information.

## Run on Windows

From this folder, create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, allow scripts for this terminal only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Install dependencies and start the app:

```powershell
python -m pip install -r requirements.txt
python application.py
```

Open http://127.0.0.1:5000. Keep the terminal open while using the app and press Ctrl+C to stop it.

The app trains its small regression pipeline from `Cleaned_Car_data.csv` at startup. It no longer loads the legacy `LinearRegressionModel.pkl`, avoiding incompatibilities between scikit-learn pickle versions. The hero photography and web fonts are loaded from external services and require an internet connection; the app itself runs locally.
