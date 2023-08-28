import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle
import os
from sklearn.metrics import r2_score, mean_squared_error

# Load the saved objects using pickle from the 'data/models' folder
loaded_objects_path = 'data/models/saved_objects.pkl'
with open(loaded_objects_path, 'rb') as objects_file:
    loaded_objects = pickle.load(objects_file)

# Access the loaded objects
model = loaded_objects['model']
X_test_scaled = loaded_objects['X_test_scaled']
y_test = loaded_objects['y_test']
data = loaded_objects['data']
X_train_scaled = loaded_objects['X_train_scaled']


y_pred = model.predict(X_test_scaled)
print("y_pred", y_pred)

# Calculate the accuracy of the prediction via R-squared and MSE score
r2 = r2_score(y_test, y_pred)
print("R-squared:", r2)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
