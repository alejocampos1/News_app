import pymysql
import tkinter as tk
from tkinter import ttk

def conectar_bd():
    # Configura los detalles de conexión a tu base de datos en AWS
    db_config = {
        'host': 'database-1.c1c8yoww2ngl.us-east-1.rds.amazonaws.com',
        'user': 'admin',
        'password': '#Ferrari1',
        'database': 'database-1',
        'cursorclass': pymysql.cursors.DictCursor
    }

    # Intenta establecer la conexión
    try:
        conn = pymysql.connect(**db_config)
        if conn.open:
            print('Conexión establecida a la base de datos')
            return conn

    except pymysql.Error as e:
        print(f'Error de conexión: {e}')
        return None

def agregar_nota(conn, titulo, contenido, cintillo):
    try:
        with conn.cursor() as cursor:
            # Inserta la nueva nota en la tabla de notas
            insert_query = "INSERT INTO notas (titulo, contenido, cintillo) VALUES (%s, %s, %s);"
            cursor.execute(insert_query, (titulo, contenido, cintillo))
        conn.commit()
        print('Nota agregada correctamente.')

    except pymysql.Error as e:
        print(f'Error al agregar la nota: {e}')

def guardar_nota():
    titulo = entry_titulo.get()
    contenido = text_contenido.get("1.0", tk.END)
    cintillo = entry_cintillo.get()

    # Establece la conexión a la base de datos
    conexion = conectar_bd()
    if conexion is None:
        return

    # Agrega la nota a la base de datos
    agregar_nota(conexion, titulo, contenido, cintillo)

    # Cierra la conexión
    if conexion.open:
        conexion.close()
        print('Conexión cerrada')

    # Limpiar los campos después de agregar la nota
    entry_titulo.delete(0, tk.END)
    text_contenido.delete("1.0", tk.END)
    entry_cintillo.delete(0, tk.END)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Aplicación de Notas")

# ... (código de la interfaz gráfica sigue igual)

# Iniciar el bucle de eventos
root.mainloop()
