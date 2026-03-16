from flask import Flask, request, jsonify
import joblib
import numpy as np
import sys
import os

# allow importing from parent folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.db_config import get_connection

app = Flask(__name__)

# Load trained model
model = joblib.load("../model/churn_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    tenure = data["tenure"]
    monthly_charges = data["monthly_charges"]

    prediction = model.predict([[tenure, monthly_charges]])

    result = "Yes" if prediction[0] == 1 else "No"

    # store result in database
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO predictions (tenure, monthly_charges, prediction)
    VALUES (%s,%s,%s)
    """

    cursor.execute(query, (tenure, monthly_charges, result))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)