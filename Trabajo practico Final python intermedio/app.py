#  Proyecto CRUD con Interfaz Gráfica
# Tema: Gestor de Cursos, Profesores y Estudiantes
# Librerías usadas: Tkinter y SQLite3

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


# Creamos la base de datos y las tablas


conn = sqlite3.connect("escuela.db")
c = conn.cursor()

# Tabla Profesores
c.execute('''CREATE TABLE IF NOT EXISTS profesores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    dni TEXT NOT NULL UNIQUE
)''')

# Tabla Cursos
c.execute('''CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    profesor_id INTEGER,
    FOREIGN KEY (profesor_id) REFERENCES profesores(id)
)''')

# Tabla Estudiantes
c.execute('''CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    curso_id INTEGER,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
)''')

conn.commit()
conn.close()


#  Funciones CRUD


def agregar_profesor():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = entry_dni.get()
    if nombre and apellido and dni:
        conn = sqlite3.connect("escuela.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO profesores (nombre, apellido, dni) VALUES (?, ?, ?)", (nombre, apellido, dni))
            conn.commit()
            messagebox.showinfo("Éxito", "Profesor agregado")
            entry_nombre.delete(0, tk.END)
            entry_apellido.delete(0, tk.END)
            entry_dni.delete(0, tk.END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "DNI duplicado")
        conn.close()
    else:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos")

def agregar_curso():
    nombre = entry_curso_nombre.get()
    profesor_id = combo_profesor.get()
    if nombre and profesor_id:
        conn = sqlite3.connect("escuela.db")
        c = conn.cursor()
        c.execute("INSERT INTO cursos (nombre, profesor_id) VALUES (?, ?)", (nombre, profesor_id.split(" - ")[0]))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Curso agregado")
        entry_curso_nombre.delete(0, tk.END)
        combo_profesor.set("")
    else:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos")

def agregar_estudiante():
    nombre = entry_est_nombre.get()
    apellido = entry_est_apellido.get()
    curso_id = combo_curso.get()
    if nombre and apellido and curso_id:
        conn = sqlite3.connect("escuela.db")
        c = conn.cursor()
        c.execute("INSERT INTO estudiantes (nombre, apellido, curso_id) VALUES (?, ?, ?)", (nombre, apellido, curso_id.split(" - ")[0]))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Estudiante agregado")
        entry_est_nombre.delete(0, tk.END)
        entry_est_apellido.delete(0, tk.END)
        combo_curso.set("")
    else:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos")


#  Interfaz Gráfic con Tkinter


ventana = tk.Tk()
ventana.title("Gestor Escolar")
ventana.geometry("400x400")

tab_control = ttk.Notebook(ventana)

tab_profesores = ttk.Frame(tab_control)
tab_cursos = ttk.Frame(tab_control)
tab_estudiantes = ttk.Frame(tab_control)

tab_control.add(tab_profesores, text='Profesores')
tab_control.add(tab_cursos, text='Cursos')
tab_control.add(tab_estudiantes, text='Estudiantes')
tab_control.pack(expand=1, fill='both')

#  PROFESS 
tk.Label(tab_profesores, text="Nombre").pack()
entry_nombre = tk.Entry(tab_profesores)
entry_nombre.pack()

tk.Label(tab_profesores, text="Apellido").pack()
entry_apellido = tk.Entry(tab_profesores)
entry_apellido.pack()

tk.Label(tab_profesores, text="DNI").pack()
entry_dni = tk.Entry(tab_profesores)
entry_dni.pack()

tk.Button(tab_profesores, text="Agregar Profesor", command=agregar_profesor).pack(pady=10)

#  CURSOS
tk.Label(tab_cursos, text="Nombre del Curso").pack()
entry_curso_nombre = tk.Entry(tab_cursos)
entry_curso_nombre.pack()

tk.Label(tab_cursos, text="Profesor").pack()
combo_profesor = ttk.Combobox(tab_cursos)
combo_profesor.pack()

def cargar_profesores():
    conn = sqlite3.connect("escuela.db")
    c = conn.cursor()
    c.execute("SELECT id, nombre || ' ' || apellido FROM profesores")
    profesores = [f"{row[0]} - {row[1]}" for row in c.fetchall()]
    combo_profesor['values'] = profesores
    conn.close()

cargar_profesores()

tk.Button(tab_cursos, text="Agregar Curso", command=agregar_curso).pack(pady=10)

# ESTUDIANTE
tk.Label(tab_estudiantes, text="Nombre").pack()
entry_est_nombre = tk.Entry(tab_estudiantes)
entry_est_nombre.pack()

tk.Label(tab_estudiantes, text="Apellido").pack()
entry_est_apellido = tk.Entry(tab_estudiantes)
entry_est_apellido.pack()

tk.Label(tab_estudiantes, text="Curso").pack()
combo_curso = ttk.Combobox(tab_estudiantes)
combo_curso.pack()

def cargar_cursos():
    conn = sqlite3.connect("escuela.db")
    c = conn.cursor()
    c.execute("SELECT id, nombre FROM cursos")
    cursos = [f"{row[0]} - {row[1]}" for row in c.fetchall()]
    combo_curso['values'] = cursos
    conn.close()

cargar_cursos()

tk.Button(tab_estudiantes, text="Agregar Estudiante", command=agregar_estudiante).pack(pady=10)

ventana.mainloop()
