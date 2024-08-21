import pandas as pd
import pickle

# Load trained model
file_to_open = open("data/models/baummethoden_lr.pickle", "rb")
trained_model = pickle.load(file_to_open)
file_to_open.close()

# Load data that we want predictions for
prediction_data = pd.read_csv('data/prediction-data.csv', sep=";")

# Make predictions and print the results
print(trained_model.predict(prediction_data))
