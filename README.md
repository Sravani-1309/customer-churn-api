# Customer Churn Prediction API

## Overview

Customer churn prediction helps businesses identify customers who are likely to stop using their service. Detecting churn early allows companies to take actions such as offering discounts, improving support, or providing personalized offers to retain customers.

This project builds a **Machine Learning model** that predicts whether a customer will churn based on features like **tenure, monthly charges, and total charges**.
The trained model is deployed using a **REST API built with FastAPI**, and prediction results are stored in a **MySQL database**.

The API allows users to send customer data and receive churn predictions in real time.

---

## Tech Stack

* **Python** – Core programming language
* **FastAPI** – REST API framework
* **Scikit-learn** – Machine learning model training
* **Pandas** – Data processing and analysis
* **MySQL** – Database for storing customer data and predictions
* **Joblib** – Model serialization

---

## Project Structure

```
customer-churn-api
├── dataset
│   └── churn.csv
├── model
│   └── train_model.py
├── saved_models
│   └── churn_model.pkl
├── api
│   └── app.py
├── database
│   └── db_config.py
├── requirements.txt
├── README.md
└── .gitignore
```

**dataset/** – Contains customer dataset used for training the ML model
**model/** – Contains model training script and saved model
**api/** – FastAPI application providing prediction endpoints
**database/** – MySQL database connection configuration

---

## Machine Learning Model

The churn prediction model is built using **Logistic Regression**.

Input features used for prediction:

* Tenure (Number of months the customer stayed)
* Monthly Charges
* Total Charges

The model is trained using **Scikit-learn** and saved using **Joblib** so that the API can load it for real-time predictions.

Example scenarios:

Example 1
Customer with **short tenure and high monthly charges** → Higher churn risk.

Example 2
Customer with **long tenure and stable payments** → Lower churn risk.

---

## Database

MySQL is used to store customer records and prediction results.

Example table structure:

customers

* id
* tenure
* monthly_charges
* total_charges
* churn_prediction

Example query:

SELECT * FROM customers WHERE churn_prediction = 1;

This query retrieves customers who are predicted to churn.

---

## Installation

1. Clone the repository

2. Navigate to the project folder

3. Create a virtual environment

4. Activate the virtual environment

5. Install dependencies

## Run the API

Start the FastAPI server

Open the API documentation in your browser:

http://127.0.0.1:8000/docs

FastAPI automatically generates interactive API documentation using Swagger UI.

---

## API Endpoint

POST /predict

Example request:

{
 "tenure": 24,
 "monthly_charges": 45
}

Example response:

{
    "prediction": "No"
}

Prediction values:
No → Customer likely to stay
Yes → Customer likely to churn

---
