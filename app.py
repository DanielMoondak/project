from flask import Flask, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/data')
def get_data():
    csv_path = os.path.join('data', 'wifi.csv')
    df = pd.read_csv(csv_path)
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
