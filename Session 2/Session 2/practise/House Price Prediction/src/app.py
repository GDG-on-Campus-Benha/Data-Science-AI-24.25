import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="House Price Predictor", 
    page_icon="🏠", 
)

# Load preprocessing artifacts
@st.cache_resource
def load_model_and_artifacts():
    """Load saved model, scaler, and feature names"""
    try:
        model = joblib.load('trained_model.pkl')
        scaler = joblib.load('scaler.pkl')
        
        # Load feature names
        with open('feature_names.txt', 'r') as f:
            feature_names = f.read().splitlines()
        
        return model, scaler, feature_names
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, None

# Main app
def main():
    st.title("🏠 House Price Prediction")
    
    # Load model
    model, scaler, feature_names = load_model_and_artifacts()
    
    if model is None:
        st.error("Could not load the model. Please check your model files.")
        return
    
    # Input features
    st.header("Input House Features")
    
    # Collect numerical inputs
    area = st.number_input(
        "Area (sq ft)", 
        min_value=100, 
        max_value=10000, 
        value=1500
    )
    bedrooms = st.number_input(
        "Number of Bedrooms", 
        min_value=1, 
        max_value=10, 
        value=3
    )
    bathrooms = st.number_input(
        "Number of Bathrooms", 
        min_value=1, 
        max_value=5, 
        value=2
    )
    stories = st.number_input(
        "Number of Stories", 
        min_value=1, 
        max_value=5, 
        value=2
    )
    parking = st.number_input(
        "Number of Parking Spots", 
        min_value=0, 
        max_value=5, 
        value=2
    )
    
    # Categorical inputs
    categorical_features = [
        'mainroad', 'guestroom', 'basement', 
        'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus'
    ]
    
    categorical_inputs = {}
    for feature in categorical_features:
        if feature == 'furnishingstatus':
            categorical_inputs[feature] = st.selectbox(
                "Furnishing Status", 
                ['furnished', 'semi-furnished', 'unfurnished']
            )
        else:
            categorical_inputs[feature] = st.selectbox(
                f"Does the house have {feature.replace('_', ' ')}?", 
                ['No', 'Yes']
            )
    
    # Prediction button
    if st.button("Predict House Price"):
        # Prepare input data
        input_data = {
            'area': area,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'stories': stories,
            'parking': parking,
            **categorical_inputs
        }
        
        # Convert to dataframe
        input_df = pd.DataFrame([input_data])
        
        # One-hot encode categorical columns
        input_df_encoded = pd.get_dummies(input_df)
        
        # Ensure all original features are present
        for col in feature_names:
            if col not in input_df_encoded.columns:
                input_df_encoded[col] = 0
        
        # Reorder columns to match training data
        input_df_encoded = input_df_encoded[feature_names]
        
        # Scale input
        input_scaled = scaler.transform(input_df_encoded)
        
        # Predict
        predicted_price = model.predict(input_scaled)[0]
        
        # Display results
        st.subheader("Prediction Results")
        st.metric(
            label="Estimated House Price", 
            value=f"${predicted_price:,.2f}"
        )

if __name__ == '__main__':
    main()