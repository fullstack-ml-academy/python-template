import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle
import os

# Load the CSV file into a pandas DataFrame

data = pd.read_csv("data/auto-mpg.csv", sep=';', skipinitialspace=True)
data.dtypes

# Display the first few rows of the DataFrame
print(data.head())

y = data.loc[:,'mpg']
X = data.drop('mpg',axis=1)

#normalize data
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

#Linear Regression
model = LinearRegression()
model.fit(X_scaled,y)

# save the model to disk
model_path = 'data/models/model.pkl'
with open(model_path, 'wb') as model_file:
    pickle.dump(model, model_file)


