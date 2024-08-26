import pandas as pd
import pickle

# Load trained model
with open("data/models/baummethoden_lr.pickle", "rb") as file_to_open:
    trained_model = pickle.load(file_to_open)

# Load data that we want predictions for
prediction_data = pd.read_csv('data/prediction-data.csv', sep=";")

# Ensure column names match those used in training
expected_columns = ['zylinder', 'ps', 'gewicht', 'beschleunigung', 'baujahr']
if not all(col in prediction_data.columns for col in expected_columns):
    raise ValueError(f"Prediction data must contain these columns: {expected_columns}")

# Make predictions and print the results
predictions = trained_model.predict(prediction_data[expected_columns])
print(predictions)

# Optional: Create a DataFrame with predictions and input features
result_df = prediction_data.copy()
result_df['predicted_mpg'] = predictions
print(result_df)
