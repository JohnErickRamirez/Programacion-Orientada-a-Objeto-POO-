import tkinter as tk
from tkinter import ttk # Importamos ttk para usar el Treeview
from tkinter import messagebox as mb
from tkinter import scrolledtext as st # Importamos scrolledtext para el campo de texto
import articulos # Importamos la clase Articulos

class formularioarticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Formulario Artículo")
        self.cuaderno1=ttk.Notebook(self.ventana1)
        self.cargar_articulos()
        self.consultar_por_codigo()
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    
    def cargar_articulos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Cargar Artículos")
        self.labelFrame1=ttk.LabelFrame(self.pagina1, text="Cargar Artículo")
        self.labelFrame1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelFrame1, text="Descripcion: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncargar=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelFrame1, textvariable=self.descripcioncargar)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelFrame1, text="Precio: ")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocargar=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelFrame1, textvariable=self.preciocargar)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4) 
        self.boton1=ttk.Button(self.labelFrame1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=0, row=2, padx=4, pady=4)

    def agregar (self):
       datos=(self.descripcioncargar.get(), self.preciocargar.get())
       self.articulo1.alta(datos)
       mb.showinfo("Informacion", "los datos fueron cargados correctamente")
       self.descripcioncargar.set("")
       self.preciocargar.set("")

    def consultar_por_codigo(self):
        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consultar por Código")
        self.labelFrame2=ttk.LabelFrame(self.pagina2, text="Articulo")
        self.labelFrame2.grid(column=0, row=0, padx=5, pady=0)
        self.label3=ttk.Label(self.labelFrame2, text="Código: ")
        self.label3.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelFrame2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelFrame2, text="Descripción: ")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelFrame2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelFrame2, text="Precio: ")
        self.label3.grid(column=0, row=2, padx=4, pady=4)  
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelFrame2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelFrame2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=0, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consultar(datos)
        if len (respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set("")
            self.precio.set("")
            mb.showinfo("Informacion", "No se encontraron resultados")

    def listado_completo(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado Completo")
        self.labelFrame3=ttk.LabelFrame(self.pagina3, text="Articulos")
        self.labelFrame3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelFrame3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scroll=st.ScrolledText(self.labelFrame3, width=30, height=10)
        self.scroll.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta = self.articulo1.recuperar_todo()
        self.scroll.delete(1.0, tk.END)  # Limpiamos el campo de texto antes de mostrar los resultados
        for fila in respuesta:
            self.scroll.insert(tk.END, "Código: " + str(fila[0]) + "\nDescripción: " + str(fila[1]) + "\nPrecio: " + str(fila[2]) + "\n\n")

aplicacion1 = formularioarticulos()