from flask import Flask, Response
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return {'hello visitor': 'welocme to this page'}

@app.route("/hello_world", methods = ['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/training")
def training_data():
    return "<p>Hier folgt Training data!</p>"

loaded_objects_path = 'data/models/saved_objects.pkl'
with open(loaded_objects_path, 'rb') as objects_file:
    loaded_objects = pickle.load(objects_file)

# Access the loaded objects
model = loaded_objects['model']
X = loaded_objects['X']
y = loaded_objects['y']
data = loaded_objects['data']
X_scaled = loaded_objects['X_scaled']

