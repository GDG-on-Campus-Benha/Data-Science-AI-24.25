# 📊Udemy-Courses-Analysis-Project📊

Udemy Courses Analysis Project that uses machine learning to predict the courses price + Data Preprocessing + Power BI for Building an Interactive Dashboard + Web Deployment using Streamlit.🤩



# Table of Contents
1. **Introduction**
2. **Overview Dashboard using Power BI**
4. **Dataset**
5. **Machine Learning for classify the course rate**
6. **Web Application Deployment**
7. **The Usage**

# Intoduction🤌
 In this Project, we delve into the vast array of courses available on Udemy to extract valuable insights and provide a comprehensive analysis. With the proliferation of online learning platforms like Udemy, understanding the trends, patterns, and characteristics of courses can offer valuable guidance for both learners and instructors.📈


# Overview Dashboard using Power BI📈

This project addresses another businees problem In this context, I see myself as a data analyst employed at Udemy. The task involves visualizing data to help readers comprehend how countries have historically performed in The puplished courses in Udemy.

**To resolve this business problem using PBI, I followed several steps:**

1. use power query
2. add a visuals and plots 
3. gain simple insights from the dataset



# Data Set Content🤔
Here, I have extracted data related to 10k courses which come under the development category on Udemy's website. The 17 columns in the dataset can be used to gain insights related to:


**id**: The unique identifier assigned to each course in the dataset.

**title**: The title or name of the course as listed on Udemy's platform.

**url**: The URL of the course on Udemy's website.

**is_paid**: A boolean value indicating whether the course is paid (True) or free (False).

**num_subscribers**: The number of individuals who have subscribed to the course.

**avg_rating**: The average rating of the course based on user reviews.

**avg_rating_recent**: The recent changes in the average rating of the course.

**num_reviews**: The total number of reviews or ratings that the course has received.

**is_wishlisted**: Indicates whether the course is wishlisted by users (True) or not (False).

**num_published_lectures**: The total number of lectures available in the course.

**num_published_practice_tests**: The number of practice tests included in the course.

**created**: The timestamp indicating the creation time of the course.

**published_time**: The timestamp indicating the time when the course was published.

**discounted_price_amount**: The discounted price at which the course is being offered.

**discounted_price_currency**: The currency corresponding to the discounted price of the course.

**discounted_price_price_string**: A formatted string representing the discounted price of the course.

**price_detail_amount**: The original price of the course before any discounts.

**price_detail_currency**: The currency corresponding to the original price of the course.

**price_detail_price_string**: A formatted string representing the original price of the course.




# Machine Learning for classify the course rate 🧠

**EDA and data cleaning**
1. Drop unnecessary columns
2. Handel missing values
3. Feature Engineering
4. Label encoding for categorical values
5. Scaling
6. Use Random forest regressor for predict the course price
7. Evaluate the model performance


# Web Application Deployment
### Uses a Streamlit licrary to deploy our machine learning model for prediction and to navigate our dataset using mulyiple pages:
1. *Predict*: a page to predict the course price using the machine learning model 
2. *Dataset Insights*: gain an insights about the dataet using description and summary statistics methods 
3. *Model Performance*: display the performance and metrices of our regression model

# Usage of web application
1. Ensure you install the requierments libraries exists in the requierments.txt file 
2. Run all python scripts in the 'src' folde
3. Ensure you run the "App.py" python script successfully
4. Open the terminal and run the following bash command:
``` Bash
    cd 'path\src'
    streamlit run App.py
```

