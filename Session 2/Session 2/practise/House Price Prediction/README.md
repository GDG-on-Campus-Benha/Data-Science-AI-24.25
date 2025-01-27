# House Price Prediction Streamlit App

## Project Overview
This project demonstrates a complete machine learning workflow for house price prediction using Streamlit for deployment.

## Project Structure
```
Project/
├── workspace/
│   └── notebook.ipynb
├── src/
│   ├── app.py                  # Streamlit web application
│   ├── preprocessing.py        # Data preprocessing script
│   ├── model.py                # Model training script
│   └── trained_model.pkl       # Saved pre-trained model
├── dataset/
│   └── housing_data.csv        # Dataset for training
├── README.md                   # Project documentation
└── requirements.txt            # Project dependencies
```

## Setup and Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
streamlit run src/app.py
```

## Model Details
- Algorithm: Random Forest Regression
- Features: Area, Bedrooms, Bathrooms, Stories, etc.
- Performance Metrics available in model training logs

## Deployment Best Practices
- Model versioning
- Preprocessing artifact saving
- Interactive web interface
- Feature importance visualization

## Contributions
Feel free to fork and improve the project!