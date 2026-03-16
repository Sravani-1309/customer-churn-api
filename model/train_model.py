import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("../dataset/churn.csv")

# Convert churn column to numeric
data['Churn'] = data['Churn'].map({'Yes':1,'No':0})

# Select features
X = data[['tenure','MonthlyCharges']]
y = data['Churn']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train,y_train)

# Save model
joblib.dump(model,"churn_model.pkl")

print("Model trained and saved")