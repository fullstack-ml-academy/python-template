from flask import Flask, Response, request
import pandas as pd
import numpy as np
import os
from flask_cors import CORS
import pickle

# Access the loaded objects
loaded_objects_path = 'data/models/saved_objects.pkl'
with open(loaded_objects_path, 'rb') as objects_file:
    loaded_objects = pickle.load(objects_file)

model = loaded_objects['model']
X_train_scaled = loaded_objects['X_train_scaled']
y_test = loaded_objects['y_test']
data = loaded_objects['data']
X_test_scaled = loaded_objects['X_test_scaled']

training_data_df = pd.read_csv("data/auto-mpg.csv", sep=';', skipinitialspace=True)
#print(training_data_df.head)

print("shape trainings data", training_data_df.shape)

#start application
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return {'hello visitor': 'welocme to this page'}

@app.route("/hello_world", methods = ['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/training_data", methods = ['GET'])
def training_data():
    return Response(training_data_df.to_json(), mimetype='application/json')

@app.route("/predict", methods = ['GET'])
def predict():
    #get parameters
    zylinder = request.args.get ('zylinder')
    ps = request.args.get('ps')
    gewicht = request.args.get('gewicht')
    beschleunigung = request.args.get('beschleunigung')
    baujahr = request.args.get('baujahr')

    #make prediction
    prediction = model.predict([zylinder, ps, gewicht, beschleunigung, baujahr])
    return {'predicted miles per gallon:': int(prediction.item())}

# cwd = os.getcwd()  # Aktuelles Arbeitsverzeichnis abrufen
# print("Current Working Directory:", cwd)


