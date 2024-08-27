import pickle
import numpy as np

model_path = 'data/models/linear_regression_model.pkl'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

input_data = np.array([[8, 130, 3504, 12.0, 70]])  # Beispiel: Gewicht = 3000 lbs

prediction = model.predict(input_data)

print(f'Vorhersage für MPG bei einem Gewicht von {input_data[0][0]} lbs: {prediction[0]}')
