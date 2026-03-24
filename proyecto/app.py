@app.route('/')
def index():
    try:
        conn = get_db_connection()

        restaurante = conn.execute('SELECT * FROM restaurante LIMIT 1').fetchone()
        menu = conn.execute(
            "SELECT * FROM menu_almuerzo WHERE fecha = '2026-03-22'"
        ).fetchall()

        conn.close()

        return render_template('index.html', restaurante=restaurante, menu=menu)

    except Exception as e:
        return f"ERROR REAL: {e}"
