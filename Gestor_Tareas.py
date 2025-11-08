import os
import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
import shutil  # Para copiar archivos

# Nombre de la base de datos
DB_NAME = 'tareas.db'

# Función para inicializar la base de datos
def crear_base_datos():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                descripcion TEXT,
                realizada INTEGER,
                responsable TEXT
            )
        ''')
        conn.commit()
        conn.close()
        print(f"Base de datos creada en: {os.path.abspath(DB_NAME)}")  # Imprimir ruta de la base de datos
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear la base de datos: {e}")

# Función para verificar si la base de datos existe, y crearla si no
def verificar_base_datos():
    if not os.path.exists(DB_NAME):
        crear_base_datos()

# Función para registrar una tarea
def registrar_tarea():
    verificar_base_datos()
    fecha = simpledialog.askstring("Input", "Ingrese la fecha (YYYY-MM-DD):")
    descripcion = simpledialog.askstring("Input", "Ingrese la descripción:")
    responsable = simpledialog.askstring("Input", "Ingrese el responsable:")
    if fecha and descripcion and responsable:
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Tareas (fecha, descripcion, realizada, responsable)
                VALUES (?, ?, ?, ?)
            ''', (fecha, descripcion, 0, responsable))  # realizada = 0 (no realizada)
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Tarea registrada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la tarea: {e}")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

# Función para eliminar tareas realizadas
def eliminar_tareas_realizadas():
    verificar_base_datos()
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Tareas WHERE realizada = 1')
        conn.commit()
        conn.close()
        messagebox.showinfo("Información", "Tareas realizadas eliminadas.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar las tareas: {e}")

# Función para consultar tareas
def consultar_tareas(opcion):
    verificar_base_datos()
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        if opcion == "todas":
            cursor.execute('SELECT * FROM Tareas')
        elif opcion == "responsable":
            responsable = simpledialog.askstring("Input", "Ingrese el nombre del responsable:")
            cursor.execute('SELECT * FROM Tareas WHERE responsable = ?', (responsable,))
        tareas = cursor.fetchall()
        conn.close()
        if tareas:
            resultado = "\n".join([f"ID: {t[0]}, Fecha: {t[1]}, Descripción: {t[2]}, Realizada: {'Sí' if t[3] else 'No'}, Responsable: {t[4]}" for t in tareas])
            messagebox.showinfo("Tareas", resultado)
        else:
            messagebox.showinfo("Tareas", "No se encontraron tareas.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo consultar las tareas: {e}")

# Función para exportar la base de datos a un nuevo archivo
def exportar_base_datos():
    verificar_base_datos()
    nuevo_archivo = simpledialog.askstring("Input", "Ingrese el nombre del nuevo archivo de base de datos (sin extensión):")
    if nuevo_archivo:
        nuevo_archivo += '.db'  # Añadir la extensión .db
        try:
            shutil.copy(DB_NAME, nuevo_archivo)  # Copiar el archivo de base de datos
            messagebox.showinfo("Información", f"Base de datos exportada a {nuevo_archivo} correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar la base de datos: {e}")
    else:
        messagebox.showwarning("Advertencia", "El nombre del archivo no puede estar vacío.")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas Pendientes")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Verificar la base de datos al iniciar
verificar_base_datos()

# Estilo de fuente
font_style = ("Arial", 12)

# Marco para organizar los botones
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Botones
btn_crear_db = tk.Button(frame, text="Crear Base de Datos", command=crear_base_datos, bg="#4CAF50", fg="white", font=font_style)
btn_crear_db.pack(pady=5, padx=10, fill='x')
btn_registrar_tarea = tk.Button(frame, text="Registrar Tarea", command=registrar_tarea, bg="#2196F3", fg="white", font=font_style)
btn_registrar_tarea.pack(pady=5, padx=10, fill='x')
btn_eliminar_realizadas = tk.Button(frame, text="Eliminar Tareas Realizadas", command=eliminar_tareas_realizadas, bg="#f44336", fg="white", font=font_style)
btn_eliminar_realizadas.pack(pady=5, padx=10, fill='x')
btn_consultar_todas = tk.Button(frame, text="Consultar Todas las Tareas", command=lambda: consultar_tareas("todas"), bg="#FF9800", fg="white", font=font_style)
btn_consultar_todas.pack(pady=5, padx=10, fill='x')
btn_consultar_responsable = tk.Button(frame, text="Consultar Tareas por Responsable", command=lambda: consultar_tareas("responsable"), bg="#9C27B0", fg="white", font=font_style)
btn_consultar_responsable.pack(pady=5, padx=10, fill='x')
btn_exportar_db = tk.Button(frame, text="Exportar Base de Datos", command=exportar_base_datos, bg="#FFC107", fg="white", font=font_style)
btn_exportar_db.pack(pady=5, padx=10, fill='x')

# Ejecutar la aplicación
root.mainloop()
