import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle
import os



y_pred = model.predict(X_scaled)
print(accuracy_score(y, y_pred))
score = model.score(y_pred,y)
print('Score:', score)
