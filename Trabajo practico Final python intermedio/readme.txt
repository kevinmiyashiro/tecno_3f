# Gestor Escolar - CRUD con Tkinter y SQLite

Esta es una aplicación de escritorio hecha en Python que permite registrar profesores, cursos y estudiantes, con una base de datos relacional en SQLite y una interfaz gráfica con Tkinter.

## ¿Qué hace la app?

- Permite cargar profesores (nombre, apellido y DNI).
- Permite crear cursos asignando un profesor.
- Permite registrar estudiantes y asociarlos a un curso.

Todos los datos quedan almacenados en una base local llamada `escuela.db`.

## Tecnologías utilizadas

- **Python 3**
- **Tkinter**: para la interfaz gráfica
- **SQLite3**: para la base de datos
- **ttk**: para pestañas y desplegables más modernos

## Cómo usarla

1. Asegurate de tener Python instalado.
2. Abrí el archivo `app.py` con un editor como VS Code.
3. Ejecutalo con:

```bash
python app.py