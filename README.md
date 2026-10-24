<div align="center">

# 🚗 Auto Worth

**A machine learning regression model that estimates used-car prices from mileage, purchase year, and car model.**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

</div>

---

## 📖 Overview

Buying or selling a used car often comes down to one question: what is a fair price? This project builds a supervised regression model that predicts a car's price from its key attributes, and wraps it in a simple web interface so anyone can try it.

It covers the full ML workflow: data cleaning, exploratory data analysis, feature engineering, model training with Scikit-learn pipelines, and evaluation.

## 📊 Results

| Metric | Score |
|---|---|
| R² Score | **[0.85 — replace with your exact value]** |
| MAE | [add value] |
| RMSE | [add value] |

> Replace these with the exact numbers from your notebook's evaluation cell.

## 🔍 Features Used

| Feature | Description |
|---|---|
| Mileage | Distance the car has been driven |
| Purchase Year | Year the car was bought, used to derive age |
| Car Model | Make/model of the car (encoded as a categorical feature) |
| **Target: Price** | The value the model predicts |

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib / Seaborn
- **Environment:** Jupyter Notebook
- **Interface:** HTML front end [add Flask / Streamlit / other if used]

## 🧪 Methodology

1. **Data cleaning:** handle missing values, duplicates, and inconsistent entries
2. **Exploratory data analysis:** explore distributions, correlations, and outliers
3. **Preprocessing:** encode categorical variables and scale numeric features
4. **Modeling:** train regression models using Scikit-learn pipelines
5. **Evaluation:** compare models on a held-out test set using R², MAE, and RMSE

## 📂 Project Structure

```
CarPricePredictor/
├── data/              # Dataset (or link to the source below)
├── notebooks/         # EDA and model training notebooks
├── templates/         # HTML front end
├── app.py             # Application entry point
├── requirements.txt
└── README.md
```

> Adjust this tree to match your actual files.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
git clone https://github.com/SarthakNere/CarPricePredictor.git
cd CarPricePredictor
pip install -r requirements.txt
```

### Run the app

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

### Explore the notebook

```bash
jupyter notebook
```

Open the notebook in `notebooks/` to see the full analysis and training process.

## 📁 Dataset

- **Source:** [add dataset name and link, e.g. Kaggle]
- **Size:** [number of rows] records, [number of columns] columns

## 🔮 Future Improvements

- [ ] Try ensemble models (Random Forest, Gradient Boosting) and compare
- [ ] Add hyperparameter tuning with cross-validation
- [ ] Include more features such as fuel type and transmission
- [ ] Deploy the app online

## 👤 Author

**Sarthak Nere**
- GitHub: [@SarthakNere](https://github.com/SarthakNere)
- LinkedIn: [linkedin.com/in/sarthaknere](https://linkedin.com/in/sarthaknere)
