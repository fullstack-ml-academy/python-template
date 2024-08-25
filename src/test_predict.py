import unittest
import pandas as pd
import pickle
import os
from predict import trained_model

class TestPredict(unittest.TestCase):

    def setUp(self):
        # Create a small sample dataset for testing
        self.test_data = pd.DataFrame({
            'zylinder': [4, 6, 8],
            'ps': [90, 110, 130],
            'gewicht': [2000, 2500, 3000],
            'beschleunigung': [15, 12, 10],
            'baujahr': [70, 75, 80]
        })

    def test_model_loaded(self):
        # Test if the model is loaded correctly
        self.assertIsNotNone(trained_model)

    def test_prediction_shape(self):
        # Test if the prediction returns the expected number of results
        predictions = trained_model.predict(self.test_data)
        self.assertEqual(len(predictions), len(self.test_data))

    def test_prediction_type(self):
        # Test if the predictions are of the expected type (float)
        predictions = trained_model.predict(self.test_data)
        self.assertTrue(all(isinstance(pred, float) for pred in predictions))

    def test_prediction_range(self):
        # Test if the predictions are within a reasonable range (e.g., 0-50 mpg)
        predictions = trained_model.predict(self.test_data)
        self.assertTrue(all(0 <= pred <= 50 for pred in predictions))

if __name__ == '__main__':
    unittest.main()
