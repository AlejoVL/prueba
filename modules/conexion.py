import sqlite3

class Conexion:

    def __init__(self):
        self.DataBase = "db/personas.db"
        self.conexion = sqlite3.connect(self.DataBase)
        self.cursor = self.conexion.cursor()

    def CloseConexion(self):
        self.conexion.commit()
        self.conexion.close()