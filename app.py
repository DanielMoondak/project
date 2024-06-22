from flask import Flask, jsonify, send_from_directory, render_template
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'  # Actualiza con tu host MySQL
app.config['MYSQL_USER'] = 'id22349349_daniel'  # Actualiza con tu usuario MySQL
app.config['MYSQL_PASSWORD'] = 'Dani123$'  # Actualiza con tu contraseña MySQL
app.config['MYSQL_DB'] = 'id22349349_dashboard'  # Actualiza con tu base de datos MySQL

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

# Ruta para obtener datos desde la base de datos MySQL y devolverlos como JSON
@app.route('/data')
def get_data():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM wifi")
        data = cur.fetchall()
        cur.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Devuelve un error 500 en caso de excepción

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
