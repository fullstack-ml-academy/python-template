import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv('data/auto-mpg.csv', delimiter=';')
X, y = data.drop(columns=['mpg'], axis=1), data.mpg

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error on Test Data: {mse}")

model_dir = 'data/models'
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, 'linear_regression_model.pkl')
with open(model_path, 'wb') as model_file:
    pickle.dump(model, model_file)

print(f"Model saved to {model_path}")

