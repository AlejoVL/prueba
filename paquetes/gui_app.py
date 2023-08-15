import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from modules.consultas import create_table, delete_table
from modules.consultas import Persona, guardar_p, recorrer_array, Editar, Eliminar

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="inicio", menu=menu_inicio)

    menu_inicio.add_command(label="Crear tabla", command=create_table)
    menu_inicio.add_command(label="Eliminar tabla", command=delete_table)
    menu_inicio.add_command(label="salir", command=root.destroy)


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=500, height=500, bg="#581845")
        self.root = root 
        self.pack()
        self.id = None
        self.campos()
        self.desabilitar_campos()
        self.tabla_personas()

    def campos(self):
        
        #Titulos
        self.label_name = tk.Label(self, text= "Nombre")
        self.label_name.config(font= ("Arial", 12, "bold"))
        self.label_name.grid(row=0, column=0, padx=10, pady=10)

        self.label_direccion = tk.Label(self, text= "Direccion")
        self.label_direccion.config(font= ("Arial", 12, "bold"))
        self.label_direccion.grid(row=1, column=0, padx=10, pady=10)

        self.label_direccion = tk.Label(self, text= "Edad")
        self.label_direccion.config(font= ("Arial", 12, "bold"))
        self.label_direccion.grid(row=2, column=0, padx=10, pady=10)

        #Campos de valor
        self.valor_name = tk.StringVar()
        self.entry_name = tk.Entry(self, textvariable=self.valor_name)
        self.entry_name.config(width=50)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.valor_direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable=self.valor_direccion)
        self.entry_direccion.config(width=50)
        self.entry_direccion.grid(row=1, column=1, padx=10, pady=10)

        self.valor_edad = tk.StringVar()
        self.entry_edad = tk.Entry(self, textvariable=self.valor_edad)
        self.entry_edad.config(width=50)
        self.entry_edad.grid(row=2, column=1, padx=10, pady=10)

        #Botones
        self.btn_nuevo = tk.Button(self, text="Nuevo")
        self.btn_nuevo.config(width=20, bg="#AF4", activebackground="#00f",cursor="star" , command=self.nuevo_copia)
        self.btn_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.btn_guardar = tk.Button(self, text="Guardar")
        self.btn_guardar.config(width=20, bg="#A4F", activebackground="#550", command= self.guardar)
        self.btn_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.btn_eliminar = tk.Button(self, text="Eliminar")
        self.btn_eliminar.config(width=20,bg="#F30",cursor="pirate" , activebackground="#FA4" ,command=self.desabilitar_campos)
        self.btn_eliminar.grid(row=3, column=2, padx=10, pady=10)        

    def nuevo(self):

        self.entry_name.config(state="normal")
        self.entry_direccion.config(state="normal")
        self.entry_edad.config(state="normal")
        self.btn_eliminar.config(state="normal")
        self.btn_guardar.config(state="normal")

    def nuevo_copia(self):

        self.id = None
        self.entry_name.config(state="normal")
        self.entry_direccion.config(state="normal")
        self.entry_edad.config(state="normal")
        self.btn_eliminar.config(state="normal")
        self.btn_guardar.config(state="normal")

    def guardar(self):
        self.nombre = self.entry_name.get()             
        self.direccion = self.entry_direccion.get()             
        self.edad = self.entry_edad.get()             
        dato = Persona(self.nombre, self.direccion, self.edad)
        
        if self.id == None:
            guardar_p(dato)
        else:
            Editar(dato, self.id)

        self.tabla_personas()

        self.desabilitar_campos()

    def desabilitar_campos(self):
        self.valor_name.set("")
        self.valor_direccion.set("")
        self.valor_edad.set("")

        self.entry_name.config(state="disabled")
        self.entry_direccion.config(state="disabled")
        self.entry_edad.config(state="disabled")

        self.btn_eliminar.config(state="disabled")
        self.btn_guardar.config(state="disabled")

    def tabla_personas(self):

        # recuperacion de los datos
        self.lista = recorrer_array()

        self.tabla = ttk.Treeview(self)
        self.tabla.config(columns=('Nombre', 'Direccion', 'Edad'))
        self.tabla.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        #scrollbar para la tabla si exede los 10 registros
        self.scroll = ttk.Scrollbar(self)
        self.scroll.config(orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Dirección")
        self.tabla.heading("#3", text="Edad")

        #Iterar la lista de personas
        for p in self.lista:
            self.tabla.insert('', p[0], text= p[0], values=(p[1], p[2], p[3]))


        #Botones de la tabla
        self.btn_nuevo = tk.Button(self, text="Editar")
        self.btn_nuevo.config(width=20, bg="#AF4", activebackground="#00f", command=self.Editar_data)
        self.btn_nuevo.grid(row=5, column=0, padx=10, pady=10)

        self.btn_borrar = tk.Button(self, text="Eliminar")
        self.btn_borrar.config(width=20,bg="#F30",activebackground="#FA4", command=self.Eliminar_data)
        self.btn_borrar.grid(row=5, column=1, padx=10, pady=10)

    def Editar_data(self):
        
        try:
            self.id = self.tabla.item(self.tabla.selection())['text']
            self.nombre = self.tabla.item(self.tabla.selection())['values'][0]
            self.direccion = self.tabla.item(self.tabla.selection())['values'][1]
            self.edad = self.tabla.item(self.tabla.selection())['values'][2]
            self.nuevo()            

            self.entry_name.insert(0, self.nombre)
            self.entry_direccion.insert(0, self.direccion)
            self.entry_edad.insert(0, self.edad)

        except:
            titulo= 'Editor de datos'
            texto ='No se ha seleccionado ningun registro para editar'
            messagebox.showerror(titulo, texto)

    def Eliminar_data(self):
        
        try:
            self.id = self.tabla.item(self.tabla.selection())['text']                                 
            Eliminar(self.id)
            self.tabla_personas()
        
        except:
            titulo= 'Editor de datos'
            texto ='No se ha seleccionado ningun registro para eliminar'
            messagebox.showerror(titulo, texto)