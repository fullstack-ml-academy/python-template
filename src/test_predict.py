import numpy as np
from predict import model, input_data, prediction

def test_model_prediction():
    # Test if the prediction output is a float
    assert isinstance(prediction[0], float), "Prediction is not a float."

    # Test if the input data shape matches expected input
    assert input_data.shape == (1, 5), f"Input data shape is incorrect: {input_data.shape}"

    # Test if the model is not None
    assert model is not None, "Model is None, it should be loaded."

    # Test if the prediction is within a reasonable range (arbitrary check for mpg value)
    assert 0 <= prediction[0] <= 100, f"Prediction value {prediction[0]} is out of expected range."

