from flask import Flask, jsonify, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configuración de la conexión a MySQL
app.config['MYSQL_DATABASE_HOST'] = 'danielvila.000webhostapp.com'
app.config['MYSQL_DATABASE_PORT'] = 3306  # Puerto por defecto para MySQL
app.config['MYSQL_DATABASE_USER'] = 'id22349349_daniel'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Dani123$'
app.config['MYSQL_DATABASE_DB'] = 'id22349349_dashboard'

mysql = MySQL()
mysql.init_app(app)

# Ruta para servir el archivo index.html desde la carpeta static
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para servir el dashboard.html desde la carpeta templates
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Ruta para obtener datos desde la base de datos MySQL
@app.route('/data')
def get_data():
    conn = mysql.connect()
    cursor = conn.cursor()

    # Ejemplo de consulta SQL, ajusta según tu estructura de tabla
    query = "SELECT Nombre, Puntos_de_acceso, Costo_punto FROM wifi"
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    data_dict = [{'Nombre': row[0], 'Puntos_de_acceso': row[1], 'Costo_punto': row[2]} for row in data]
    return jsonify(data_dict)

if __name__ == '__main__':
    app.run(debug=True)
