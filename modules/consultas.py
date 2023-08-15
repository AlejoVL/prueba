from .conexion import Conexion
from tkinter import messagebox

class Persona:

    def __init__(self, nombre, direccion, edad):
        self.id = None
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad

    def __str__(self):
        return f"'{self.nombre}', '{self.direccion}', '{self.edad}'"

def create_table():
    conn = Conexion()

    sql = '''
    CREATE TABLE personas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(20),
        direccion VARCHAR(20),
        edad INTEGER(100)
    )
    '''
    try:
        conn.cursor.execute(sql)
        conn.CloseConexion()
        titulo = 'Crear registro'
        mensaje = 'Se creó existosamente la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = 'Crear registro'
        mensaje = 'La tabla ya está creada'
        messagebox.showwarning(titulo, mensaje)

def delete_table():
    conn = Conexion()

    sql = '''
    DROP TABLE personas;
    '''

    try:
        conn.cursor.execute(sql)
        conn.CloseConexion()
        titulo = 'Borrar registro'
        mensaje = 'Se borró exitosamente el registro'
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = 'Borrar registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)

def guardar_p(Persona):
    conn = Conexion()
    sql = f"""
    INSERT INTO personas(nombre,direccion,edad) VALUES({Persona})
    """
    try:
        conn.cursor.execute(sql)        
        conn.CloseConexion()
    
    except:
        titulo = 'Error'
        texto = 'No se ha podido realizar la insercion a la base de datos'
        messagebox.showerror(titulo, texto)

def recorrer_array():
    conn = Conexion()
    lista = []
    sql = '''
    SELECT * FROM personas
    '''

    try:
        conn.cursor.execute(sql)
        lista = conn.cursor.fetchall()       
        conn.CloseConexion()        

    except:
        titulo = 'Conexion al registro.'
        texto = 'La tabla personas no está creada en la base de datos'
        messagebox.showerror(titulo, texto)

    return lista

def Editar(Personas, id_persona):
    conn = Conexion()

    sql = f"""UPDATE personas 
    SET Nombre = '{Personas.nombre}',
    Direccion = '{Personas.direccion}',
    Edad = '{Personas.edad}'
    WHERE ID = '{id_persona}'"""

    try:
        conn.cursor.execute(sql)
        conn.CloseConexion()

    except:
        titulo= 'Editor de datos'
        texto ='No se ha podido editar'
        messagebox.showerror(titulo, texto)

def Eliminar(id_persona):
    conn = Conexion()

    sql = f"""DELETE FROM personas 
    WHERE ID = '{id_persona}
    '"""

    try:
        conn.cursor.execute(sql)
        conn.CloseConexion()

    except:
        titulo= 'Editor de datos'
        texto ='No se ha podido elimiar'
        messagebox.showerror(titulo, texto)