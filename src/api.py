from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
import joblib

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://auto-mpg-predictor.vercel.app"}})

# Modell laden
model = joblib.load('data/models/baummethoden_lr.pickle')

@app.route('/')
def index():
    return jsonify({"hello": "world"})

@app.route('/hello_world')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/training_data')
def training_data():
    data = [
        {"zylinder": 8, "ps": 130, "gewicht": 3504, "beschleunigung": 12.0, "baujahr": 70, "mpg": 18.0},
        {"zylinder": 8, "ps": 165, "gewicht": 3693, "beschleunigung": 11.5, "baujahr": 70, "mpg": 15.0},
        # Weitere Daten können hinzugefügt werden
    ]
    return jsonify(data)

@app.route('/predict', methods=['GET'])
def predict():
    # Holen der Parameter aus der Anfrage
    zylinder = request.args.get('zylinder', type=int)
    ps = request.args.get('ps', type=int)
    gewicht = request.args.get('gewicht', type=int)
    beschleunigung = request.args.get('beschleunigung', type=float)
    baujahr = request.args.get('baujahr', type=int)

    # Überprüfen, ob alle erforderlichen Parameter vorhanden sind
    if None in (zylinder, ps, gewicht, beschleunigung, baujahr):
        return jsonify({"error": "Alle Parameter (zylinder, ps, gewicht, beschleunigung, baujahr) müssen angegeben werden"}), 400

    # Umwandlung der Parameter in ein DataFrame
    import pandas as pd
    input_features = pd.DataFrame({
        'zylinder': [zylinder],
        'ps': [ps],
        'gewicht': [gewicht],
        'beschleunigung': [beschleunigung],
        'baujahr': [baujahr]
    })

    # Vorhersage mit dem geladenen Modell
    mpg_prediction = model.predict(input_features)[0]

    # Rückgabe der Vorhersage als JSON
    return jsonify({"predicted_mpg": float(mpg_prediction)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
