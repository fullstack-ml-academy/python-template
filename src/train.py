import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# CSV-Datei einlesen
data = pd.read_csv("./data/auto-mpg.csv", sep=";")

print(data.columns)  # Ausgabe der Spaltennamen zur Überprüfung

# Daten mischen
data = data.sample(frac=1, random_state=42)

# 'class'-Spalte (Zielvariable)
y_variable = data['mpg']

# Alle Spalten außer 'mpg' als Merkmale verwenden
x_variables = data.drop('mpg', axis=1)

x_train, x_test, y_train, y_test = train_test_split(
    x_variables, y_variable, test_size=0.2, random_state=42)

regressor = LinearRegression()

regressor = regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

# Modell speichern
with open("data/models/baummethoden_lr.pickle", "wb") as file_to_write:
    pickle.dump(regressor, file_to_write)

# Ausgabe der verwendeten Merkmale
print("Verwendete Merkmale:", x_variables.columns.tolist())

# Fügen Sie diese Zeile hinzu, um die Koeffizienten und ihre zugehörigen Feature-Namen auszugeben
for feature, coef in zip(x_variables.columns, regressor.coef_):
    print(f"{feature}: {coef}")
