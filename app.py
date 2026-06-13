import streamlit as st
import joblib
import numpy as np
import pandas as pd

# 1. Load the model
model = joblib.load('house_model.pkl')

st.title("🏡 California House Price Predictor")
st.write("Enter the location and property details to estimate the median house value.")

# 2. Create UI Inputs for the 8 numeric columns
col1, col2 = st.columns(2)

with col1:
    longitude = st.number_input("Longitude (e.g., -122.23)", value=-122.23)
    latitude = st.number_input("Latitude (e.g., 37.88)", value=37.88)
    housing_median_age = st.slider("Housing Median Age", min_value=1, max_value=52, value=28)
    total_rooms = st.number_input("Total Rooms in Block", value=2000)

with col2:
    total_bedrooms = st.number_input("Total Bedrooms in Block", value=400)
    population = st.number_input("Population in Block", value=1000)
    households = st.number_input("Households in Block", value=300)
    median_income = st.number_input("Median Income (in tens of thousands, e.g., 4.5)", value=4.5)

# Dropdown for the categorical column
ocean_proximity = st.selectbox(
    "Ocean Proximity", 
    ["<1H OCEAN", "INLAND", "ISLAND", "NEAR OCEAN", "NEAR BAY"]
)

# 3. Predict Button Logic
if st.button("Predict House Value"):
    
    # Create a dictionary matching your original 9 raw inputs
    input_dict = {
        'longitude': longitude,
        'latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms,
        'total_bedrooms': total_bedrooms,
        'population': population,
        'households': households,
        'median_income': median_income,
        'ocean_proximity': ocean_proximity
    }
    
    # Convert to DataFrame
    df = pd.DataFrame([input_dict])
    
    # Convert categorical text into dummy/indicator columns (0s and 1s)
    df_encoded = pd.get_dummies(df, columns=['ocean_proximity'])
    
    # Add the extra engineered features used during training.
    # The model expects 15 inputs, so we must create the same derived columns.
    df_encoded['rooms_per_household'] = df['total_rooms'] / df['households']
    df_encoded['population_per_household'] = df['population'] / df['households']
    
    expected_columns = [
        'longitude', 'latitude', 'housing_median_age', 'total_rooms',
        'total_bedrooms', 'population', 'households', 'median_income',
        'rooms_per_household', 'population_per_household',
        'ocean_proximity_<1H OCEAN', 'ocean_proximity_INLAND', 
        'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY', 
        'ocean_proximity_NEAR OCEAN'
    ]
    
    # If your notebook had slightly different dummy names, ensure they match
    # the 15 columns printed by X.columns. Fill missing ones with 0.
    for col in expected_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
            
    # Reorder columns to match the exact order your model expects
    final_input = df_encoded[expected_columns]
    
    # 4. Make prediction
    prediction = model.predict(final_input)
    
    st.success(f"💰 Estimated Median House Value: ${prediction[0]:,.2f}")