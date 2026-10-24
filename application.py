from pathlib import Path

import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Cleaned_Car_data.csv"
FEATURE_COLUMNS = ["name", "company", "year", "kms_driven", "fuel_type"]

app = Flask(__name__)
car = pd.read_csv(DATA_PATH)
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore", drop="first"),
            ["name", "company", "fuel_type"],
        ),
    ],
    remainder="passthrough",
)
model = make_pipeline(preprocessor, LinearRegression())
model.fit(car[FEATURE_COLUMNS], car["Price"])

company_models = {
    company: sorted(group["name"].dropna().unique().tolist())
    for company, group in car.groupby("company")
}
years = sorted(car["year"].dropna().astype(int).unique().tolist(), reverse=True)
fuel_types = sorted(car["fuel_type"].dropna().unique().tolist())


@app.get("/")
def dashboard():
    prices = car["Price"].dropna()
    company_counts = car["company"].value_counts().head(5)
    max_count = int(company_counts.max())
    top_companies = [
        {"name": company, "count": int(count), "width": round(count / max_count * 100)}
        for company, count in company_counts.items()
    ]
    return render_template(
        "index.html",
        active_page="dashboard",
        stats={
            "cars": len(car),
            "companies": car["company"].nunique(),
            "median_price": int(prices.median()),
            "year_range": f"{int(car['year'].min())} – {int(car['year'].max())}",
        },
        top_companies=top_companies,
        featured_cars=car.sort_values("Price", ascending=False).head(3).to_dict("records"),
    )


@app.get("/predictor")
def predictor():
    return render_template(
        "predictor.html",
        active_page="predictor",
        company_models=company_models,
        years=years,
        fuel_types=fuel_types,
    )


@app.get("/about")
def about():
    return render_template("about.html", active_page="about", stats={"cars": len(car)})


@app.post("/predict")
def predict():
    company = request.form.get("company", "").strip()
    car_model = request.form.get("car_model", "").strip()
    fuel_type = request.form.get("fuel_type", "").strip()
    year_value = request.form.get("year", "").strip()
    driven_value = request.form.get("kms_driven", "").strip()

    if company not in company_models or car_model not in company_models.get(company, []):
        return jsonify(error="Choose a valid company and matching car model."), 400
    if fuel_type not in fuel_types:
        return jsonify(error="Choose a valid fuel type."), 400

    try:
        year = int(year_value)
        kms_driven = float(driven_value.replace(",", ""))
    except ValueError:
        return jsonify(error="Enter a valid year and kilometres driven."), 400

    if year not in years or not np.isfinite(kms_driven) or kms_driven < 0:
        return jsonify(error="Year must be in the dataset range and kilometres cannot be negative."), 400

    features = pd.DataFrame(
        [[car_model, company, year, kms_driven, fuel_type]],
        columns=FEATURE_COLUMNS,
    )
    estimate = float(model.predict(features)[0])
    return jsonify(prediction=round(estimate, 2), currency="INR")


if __name__ == "__main__":
    app.run(debug=False)
