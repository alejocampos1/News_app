import mysql.connector
import tkinter as tk
from tkinter import ttk

def conectar_bd():
    # Configura los detalles de conexión a tu base de datos en AWS
    db_config = {
        'host': 'database-1.c1c8yoww2ngl.us-east-1.rds.amazonaws.com',
        'user': 'admin',
        'password': '#Ferrari1',
        'database': 'database-1'
    }

    # Intenta establecer la conexión
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print('Conexión establecida a la base de datos')
            return conn

    except mysql.connector.Error as e:
        print(f'Error de conexión: {e}')
        return None

def agregar_nota(conn, titulo, contenido, cintillo):
    try:
        cursor = conn.cursor()
        # Inserta la nueva nota en la tabla de notas
        insert_query = "INSERT INTO notas (titulo, contenido, cintillo) VALUES (%s, %s, %s);"
        cursor.execute(insert_query, (titulo, contenido, cintillo))
        conn.commit()
        print('Nota agregada correctamente.')

    except mysql.connector.Error as e:
        print(f'Error al agregar la nota: {e}')

    finally:
        cursor.close()

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
    if conexion.is_connected():
        conexion.close()
        print('Conexión cerrada')

    # Limpiar los campos después de agregar la nota
    entry_titulo.delete(0, tk.END)
    text_contenido.delete("1.0", tk.END)
    entry_cintillo.delete(0, tk.END)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Aplicación de Notas")

# Etiqueta y entrada para el título
label_titulo = tk.Label(root, text="Título:")
label_titulo.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_titulo = tk.Entry(root, width=30)
entry_titulo.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta y área de texto para el contenido
label_contenido = tk.Label(root, text="Contenido:")
label_contenido.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
text_contenido = tk.Text(root, width=30, height=5)
text_contenido.grid(row=1, column=1, padx=10, pady=5)

# Etiqueta y entrada para el cintillo
label_cintillo = tk.Label(root, text="Cintillo:")
label_cintillo.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_cintillo = tk.Entry(root, width=30)
entry_cintillo.grid(row=2, column=1, padx=10, pady=5)

# Botón para agregar nota
btn_agregar = tk.Button(root, text="Agregar Nota", command=guardar_nota)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar el bucle de eventos
root.mainloop()