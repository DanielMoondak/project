from flask import Flask, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

# Ruta para servir la página principal
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Ruta para obtener los datos del CSV
@app.route('/data')
def get_data():
    csv_path = os.path.join('data', 'wifi.csv')
    df = pd.read_csv(csv_path)
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
