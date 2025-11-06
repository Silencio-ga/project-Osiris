import sqlite3, os, random

# ruta a la base de datos (ajustala si tu estructura cambia)
DB_PATH = os.path.join(os.path.dirname(__file__), "../data/database.db")

# ==============================
#  CONEXIÓN Y CREACIÓN DE TABLA
# ==============================

# funcion para conecta a la base de datos
# devuelve 'conn' que es la conexion con la base de datos y
# devulve 'cursor' que es un objeto intermediario que permite ejecutar sentencias SQL 
def conectar():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

# funcion para crear una tabla si no existe, llamada 'eventos'
def crear_tabla_eventos():
    conn, cursor = conectar()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS eventos (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    personaje TEXT,
    evento_titulo TEXT,
    descripcion_1_1 TEXT,
    opcion_1_1 TEXT,
    opcion_2_1 TEXT,
    opcion_3_1 TEXT,
    resultado_1 TEXT,
    resultado_2 TEXT,
    resultado_3 TEXT
);
""")
    conn.commit()
    conn.close()

# ================
#  FUNCIONES CRUD
# ================

# funcion para añadir un evento
def agregar_evento(personaje,titulo, descripcion_1_1, opcion_1_1, opcion_2_1, opcion_3_1, resultado_1, resultado_2, resultado_3):
    conn, cursor = conectar()
    cursor.execute("""INSERT INTO eventos (
        personaje, evento_titulo, descripcion_1_1,
        opcion_1_1, opcion_2_1,opcion_3_1,
        resultado_1, resultado_2, resultado_3 
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
    personaje, 
    titulo, 
    descripcion_1_1,
    opcion_1_1, 
    opcion_2_1, 
    opcion_3_1,
    resultado_1, 
    resultado_2, 
    resultado_3))

    conn.commit()
    conn.close()

# funcion para devolve los datos del evento o resultados almacenados
# se puede filtra por el personaje y retona un evento aletorio
def obtener_eventos_aleatorios(personaje=None):
    conn, cursor = conectar()
    if personaje:
        cursor.execute("SELECT * FROM eventos WHERE personaje = ?",(personaje,))
    else:
        cursor.execute("SELECT * FROM eventos")
    eventos = cursor.fetchall()
    conn.close()
    return random.choice(eventos) 

# funcion para eliminar 
def eliminar_evento(id_evento):
    conn,cursor = conectar()
    cursor.execute("DELETE FROM evenetos WHERE id = ?", (id_evento,))
    conn.commit()
    conn.close()

# funcion para actualizar una fila y su campo
def actualizar_evento(id_evento, campo, nuevo_valor):
    conn, cursor = conectar()
    query = f"UPDATE eventos SET {campo} = ? WHERE id = ?"
    cursor.execute(query, (nuevo_valor, id_evento))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_tabla_eventos()
    agregar_evento(
        personaje='Eldric',
        titulo='El juramento roto...',
        descripcion_1_1= '\nEl crepúsculo cae sobre un viejo puente cubierto de ceniza. \nEn el centro, un grupo de bandidos acorrala a una mujer y a su hijo.\nEldric observa en silencio. Podría intervenir… o seguir su camino.\nLa última vez que intentó ser un héroe, su espada solo trajo muerte.\n',
        opcion_1_1='Intervenir y luchar contra los bandidos.',
        opcion_2_1='Ignorar el suceso y continuar su viaje.',
        opcion_3_1='Esperar a que los bandidos terminen, y luego saquear los restos.',
        resultado_1='Eldric derrota a los bandidos tras una dura batalla.\nLa mujer le agradece, pero él queda herido.\n“Aún hay bondad en ti, aunque la odies.” [ +15 exp ]\n',
        resultado_2='Eldric pasa de largo.\nEl eco de los gritos lo acompaña durante toda la noche.\n“Quizás salvar vidas ya no es parte de tu deber…” [ sin cambios ]\n',
        resultado_3='Eldric espera.\nCuando todo termina, rebusca entre los cuerpos.\nEncuentra una bolsa de oro… y los ojos sin vida del niño.\n“El silencio del puente pesa más que el oro.” [ +30 oro ]\n'
    )


