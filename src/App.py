import streamlit as st
import pandas as pd
from data_preprocessing import load_and_preprocess_data
from model import train_model

def load_data(): 
    df, X, y, le_title, le_wishlist, scaler = load_and_preprocess_data(r'F:\DS & AI Bootcamp Material\Project\project\dataset\dataset.csv')
    return df, X, y, le_title, le_wishlist, scaler

def main():
    st.title('Udemy Course Rating Prediction')

    # Load and preprocess data
    df, X, y, le_title, le_wishlist, scaler = load_data()

    rf, X_test, y_test, y_pred, mse, mae, r2 = train_model(X, y)

    # Sidebar for navigation
    page = st.sidebar.selectbox(
        'Navigate',
        ['Prediction', 'Model Performance', 'Dataset Insights']
    )
    
    if page == 'Prediction': 
        st.header('Course Rating Prediction')

        input_data = {} # dictionary to store user input data

        # Take user input
        available_titles = list(le_title.classes_)
        search_query = st.text_input('Search for a Course Title')
        filtered_titles = [title for title in available_titles if search_query.lower() in title.lower()] # filter titles and if it in upper case then convert it to lower case
        selected_title = st.selectbox('Select Course Title', filtered_titles if search_query else available_titles)
        input_data['title'] = selected_title

        input_data['num_subscribers'] = st.number_input('Number of Subscribers', min_value=0, value=100)
        input_data['num_reviews'] = st.number_input('Number of Reviews', min_value=0, value=10)
        input_data['num_published_practice_tests'] = st.number_input('Number of Practice Tests', min_value=0, value=0)
        input_data['price_detail__amount'] = st.number_input('Course Price', min_value=0.0, value=10.0, step=0.1)

        wishlist_status = st.selectbox('Is Wishlisted', [False, True])
        input_data['is_wishlisted'] = wishlist_status

        input_df = pd.DataFrame([input_data])

        # Encoding
        input_df['title'] = le_title.transform([input_df['title'][0]])
        input_df['is_wishlisted'] = int(input_df['is_wishlisted'][0]) # convert boolean to integer [false: 0, true: 1]

        input_df = input_df[X.columns]
        
        # Scaling
        numerical_cols = ['num_subscribers', 'num_reviews', 'price_detail__amount']
        input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

        # Prediction
        if st.button('Predict Rating'):
            prediction = rf.predict(input_df)
            st.success(f'Predicted Course Rating: {prediction[0]:.2f}')

    elif page == 'Model Performance':
        st.header('Model Performance Metrics')
        col1, col2, col3 = st.columns(3)

        # Display model performance metrics
        with col1:
            st.metric('Mean Squared Error', f'{mse:.4f}')
        with col2:
            st.metric('Mean Absolute Error', f'{mae:.4f}')
        with col3:
            st.metric('R-squared', f'{r2:.4f}')

        # Display feature importance
        st.subheader('Feature Importance') 
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': rf.feature_importances_
        }).sort_values('importance', ascending=False) 

        st.bar_chart(feature_importance.set_index('feature'))

    
    elif page == 'Dataset Insights': 
        st.header('Dataset Overview')
        
        # Display the dataset summary statistics
        st.subheader('Dataset Statistics')
        st.write(X.describe())
        
        # Display the correlation matrix
        st.subheader('Feature Correlation')
        corr_matrix = X.corr()
        st.dataframe(corr_matrix)

# Run the app
if __name__ == '__main__':
    main()
