import os
import pickle
import pytest
from train import model_path, mse, model_dir

def test_model_training():
    # Test if the model file was created
    assert os.path.exists(model_path), "Model file was not created."

    # Test if the Mean Squared Error is within a reasonable range
    assert mse < 100, f"Mean Squared Error is too high: {mse}"

def test_model_saving():
    # Test if the model directory exists
    assert os.path.exists(model_dir), "Model directory was not created."
    
    # Load the saved model and check if it's not None
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    assert model is not None, "Model could not be loaded."
