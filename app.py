from flask import Flask, jsonify, send_from_directory, render_template
from flask_mysqldb import MySQL
import pandas as pd
import os

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'id22349349_daniel'
app.config['MYSQL_PASSWORD'] = 'Dani123$'
app.config['MYSQL_DB'] = 'id22349349_dashboard'

# Inicialización de la extensión MySQL
mysql = MySQL(app)

# Ruta para servir el archivo index.html desde la carpeta static
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Ruta para servir el dashboard.html desde la carpeta templates
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Ruta para obtener datos del archivo CSV como JSON
@app.route('/data')
def get_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM wifi")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
