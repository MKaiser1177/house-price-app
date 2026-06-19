# California House Price Predictor

A standard machine learning project that predicts California house prices using a trained model and a Streamlit app deployment.

## Project Overview

- **Goal:** Predict median house value from housing block features.
- **App:** `app.py` is a Streamlit web app for entering inputs and generating price estimates.
- **Dataset:** `housing.csv` contains the original data used for analysis and training.
- **Model:** `house_model.pkl` is the saved scikit-learn model used by the app.

## Files

- `app.py` – Streamlit application for prediction.
- `house_model.pkl` – Serialized trained model.
- `housing.csv` – Raw dataset used during exploration and training.
- `main.ipynb` – Notebook with data analysis, feature engineering, and model training.
- `requirements.txt` – Python packages required to run the app and notebook.

## Setup

1. Create and activate a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

Start the Streamlit app from the project folder:

```bash
streamlit run app.py
```

Open the URL shown in the terminal to use the interactive predictor.

## Notes

- The app expects the same input features used during model training, including engineered features derived from the raw housing data.
- If you make changes to the data preprocessing or model, retrain and save `house_model.pkl` before using the app.

## Notebook

To review the data workflow and model training, open `main.ipynb` in Jupyter.

## Requirements

This project uses:

- `streamlit`
- `scikit-learn`
- `pandas`
- `numpy`
- `joblib`

Install them with `pip install -r requirements.txt`.
