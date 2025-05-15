import sqlite3

# Crear conexión
conn = sqlite3.connect("pedidos.db")
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('master', 'basico')) NOT NULL
)
""")

# Insertar usuario máster (admin / 2109)
try:
    cursor.execute("""
    INSERT INTO usuarios (nombre, username, password_hash, tipo)
    VALUES (?, ?, ?, ?)
    """, ("Administrador", "admin", "2109", "master"))
    print("✅ Usuario máster creado: admin / 2109")
except sqlite3.IntegrityError:
    print("⚠️ El usuario 'admin' ya existe.")

# Insertar usuario básico (empleado / 1234)
try:
    cursor.execute("""
    INSERT INTO usuarios (nombre, username, password_hash, tipo)
    VALUES (?, ?, ?, ?)
    """, ("Empleado", "empleado", "1234", "basico"))
    print("✅ Usuario básico creado: empleado / 1234")
except sqlite3.IntegrityError:
    print("⚠️ El usuario 'empleado' ya existe.")

# Guardar y cerrar
conn.commit()
conn.close()
