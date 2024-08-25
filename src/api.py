from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"hello": "world"})

@app.route('/hello_world')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/training_data')
def training_data():
    training_data = [1, 2, 3, 4, 5]  # Beispiel-Daten
    return jsonify(training_data)

@app.route('/predict')
def predict():
    zylinder = request.args.get('zylinder', type=int)
    ps = request.args.get('ps', type=int)
    gewicht = request.args.get('gewicht', type=int)
    beschleunigung = request.args.get('beschleunigung', type=float)
    baujahr = request.args.get('baujahr', type=int)

    result = (zylinder * ps / gewicht) * beschleunigung + baujahr * 0.1
    return jsonify({"result": result})
