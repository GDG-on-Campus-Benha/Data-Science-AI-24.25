import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

# Load dataset and preprocess data
def load_data():
    # Handle file paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(BASE_DIR, '../dataset/dataset.csv')

    # Load dataset
    df = pd.read_csv(dataset_path)

  # 3. Drop unnecessary columns
    columns_to_drop = [
        'id', 'avg_rating', 'url', 'created', 'num_published_lectures',
        'discount_price__currency', 'discount_price__amount', 'published_time',
        'is_paid', 'discount_price__price_string',
        'price_detail__currency', 'price_detail__price_string', 'avg_rating_recent'
    ]
    df.drop(columns=columns_to_drop, axis=1, inplace=True)
    
    # Encoding categorical features
    le_title = LabelEncoder()
    df['title'] = le_title.fit_transform(df['title'])

    le_wishlist = LabelEncoder()
    df['is_wishlisted'] = le_wishlist.fit_transform(df['is_wishlisted'])

    # Scaling numerical features
    scaler = StandardScaler()
    numerical_cols = ['num_subscribers', 'num_reviews', 'price_detail__amount']
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Splitting features and target
    X = df.drop(columns=['rating'])
    y = df['rating']

    return df, X, y, le_title, le_wishlist, scaler

def main():
    st.title('Udemy Course Rating Prediction')

    # Load and preprocess data
    df, X, y, le_title, le_wishlist, scaler = load_data()

    input_data = {}  # Dictionary to store user input data

    # Take user input
    available_titles = list(le_title.classes_)
    search_query = st.text_input('Search for a Course Title')
    filtered_titles = [title for title in available_titles if search_query.lower() in title.lower()]
    selected_title = st.selectbox(
        'Select Course Title',
        filtered_titles if search_query else available_titles,
        placeholder='Course Title'
    )

    if selected_title in available_titles:
        input_data['title'] = selected_title
    else:
        st.error("Invalid course title selected.")
        return

    input_data['num_subscribers'] = st.number_input('Number of Subscribers', min_value=0, value=100)
    input_data['num_reviews'] = st.number_input('Number of Reviews', min_value=0, value=10)
    input_data['num_published_practice_tests'] = st.number_input('Number of Practice Tests', min_value=0, value=0)
    input_data['price_detail__amount'] = st.number_input('Course Price', min_value=0.0, value=10.0, step=0.1)
    input_data['is_wishlisted'] = st.selectbox('Is Wishlisted', [False, True])

    # Create a DataFrame with missing columns
    input_df = pd.DataFrame([input_data])
    for col in X.columns:
        if col not in input_df.columns:
            input_df[col] = 0  # Add missing columns with default values

    # Encoding
    input_df['title'] = le_title.transform([input_df['title'][0]])
    input_df['is_wishlisted'] = int(input_df['is_wishlisted'][0])  # Convert boolean to integer

    # Align columns with X
    input_df = input_df[X.columns]

    # Scaling
    numerical_cols = ['num_subscribers', 'num_reviews', 'price_detail__amount']
    try:
        input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])
    except Exception as e:
        st.error(f"Error scaling input: {e}")
        return

    # Prediction
    if st.button('Predict Rating'):
        
            rf = joblib.load(r'F:\DS & AI Bootcamp Material\Workshop Project\project\workspace\rf_model')
            prediction = rf.predict(input_df)
            st.success(f'Predicted Course Rating: {prediction[0]:.2f}')
        

# Run the app
if __name__ == '__main__':
    main()
