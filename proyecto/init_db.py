+import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# ── Crear tablas (exactamente como pide el examen) ───────────────────────────
cursor.executescript('''
    DROP TABLE IF EXISTS restaurante;
    DROP TABLE IF EXISTS menu_almuerzo;

    CREATE TABLE restaurante (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        eslogan TEXT,
        descripcion TEXT NOT NULL,
        logo TEXT,
        imagen_portada TEXT
    );

    CREATE TABLE menu_almuerzo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha DATE NOT NULL,
        nombre_plato TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio REAL NOT NULL,
        imagen TEXT,
        disponible TEXT NOT NULL
    );
''')

# ── Datos del restaurante (1 registro) ───────────────────────────────────────
cursor.execute('''
    INSERT INTO restaurante (nombre, eslogan, descripcion, logo, imagen_portada)
    VALUES (
        'Sabor Boliviano',
        'Almuerzos caseros con tradición',
        'Restaurante especializado en comida típica boliviana, ofreciendo almuerzos completos con ingredientes frescos y atención rápida.',
        'img/logo.png',
        'img/portada.jpg'
    )
''')



cursor.executemany('''
    INSERT INTO menu_almuerzo
        (fecha, nombre_plato, descripcion, categoria, precio, imagen, disponible)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    ('2026-03-22',
     'Sopa de maní',
     'Sopa tradicional boliviana con fideo, papa y carne.',
     'Entrada',
     8.50,
     'img/sopa_mani.jpg',    # ← pon aquí tu imagen
     'Sí'),

    ('2026-03-22',
     'Silpancho',
     'Carne apanada con arroz, papa, huevo y ensalada.',
     'Plato principal',
     18.00,
     'img/silpancho.jpg',    # ← pon aquí tu imagen
     'Sí'),

    ('2026-03-22',
     'Fricasé paceño',
     'Plato típico con carne de cerdo, mote y ají amarillo.',
     'Plato principal',
     20.00,
     'img/fricase.jpg',      # ← pon aquí tu imagen (o déjalo vacío)
     'Sí'),

    ('2026-03-22',
     'Flan casero',
     'Postre suave preparado artesanalmente.',
     'Postre',
     6.00,
     'img/flan.jpg',         # ← pon aquí tu imagen
     'Sí'),
])

conn.commit()
conn.close()
print("✅ Base de datos creada correctamente con 4 platos.")