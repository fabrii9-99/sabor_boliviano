import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# ── Conexión a la base de datos ──────────────────────────────────────────────
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # permite acceder a columnas por nombre
    return conn

# ── Ruta principal ───────────────────────────────────────────────────────────
@app.route('/')
def index():
    conn = get_db_connection()

    # Consulta: información del restaurante
    restaurante = conn.execute('SELECT * FROM restaurante LIMIT 1').fetchone()

    # Consulta: menú filtrado por fecha específica
    menu = conn.execute(
        "SELECT * FROM menu_almuerzo WHERE fecha = '2026-03-22'"
    ).fetchall()

    conn.close()
    print(menu)
    return render_template('index.html', restaurante=restaurante, menu=menu)

# ── Punto de entrada ─────────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)
