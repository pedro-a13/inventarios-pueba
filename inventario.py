from tkinter import *
import os

def ventana_inicio():
	global ventana_principal
	pestas_color="DarkGrey"
	ventana_principal=Tk()
	ventana_principal.geometry("300x250")
	ventana_principal.title("Inventario")
	Label(ventana_principal,text="Escoja una opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
	Label(ventana_principal,text="").pack()
	Button(ventana_principal,text="Buscar", height="2", width="30", bg=pestas_color, command=buscar).pack()
	Label(text="").pack()
	Button(ventana_principal,text="Agregar", height="2", width="30", bg=pestas_color, command=agregar).pack()
	ventana_principal.mainloop()


def buscar():
	pestas_color="DarkGrey"
	ventana_buscar = Toplevel(ventana_principal)
	ventana_buscar.title("Buscar")
	Label(ventana_buscar,text="Codigo Del Producto", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
	Label(ventana_buscar,text="").pack()
	buscar1 = StringVar ()
	Entry(ventana_buscar,width="24", font = ('Arial',12), textvariable=buscar1).pack()
	Label(ventana_buscar,text="").pack()
	Button(ventana_buscar,text="Buscar", height="2", width="30", bg=pestas_color).pack()
	Label(ventana_buscar,text="").pack()
	ventana_buscar.geometry("300x250")

def agregar():
	
	global nos
	global codigo1
	global cantidad
	global ventana_agregar
	pestas_color="DarkGrey"
	ventana_agregar = Toplevel(ventana_principal)
	Label(ventana_agregar,text="LLene Los Datos", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
	Label(ventana_agregar,text="Nombre").pack()
	nos = StringVar ()
	Entry(ventana_agregar,width="24", font = ('Arial',12),textvariable= nos).pack()
	Label(ventana_agregar,text="Codigo").pack()
	codigo1 = StringVar ()
	Entry(ventana_agregar,width="24", font = ('Arial',12),textvariable= codigo1).pack()
	Label(ventana_agregar,text="Cantidad").pack()
	cantidad = StringVar ()
	Entry(ventana_agregar,width="24", font = ('Arial',12),textvariable= cantidad).pack()
	Label(ventana_agregar,text="").pack()
	Button(ventana_agregar,text="Agregar", height="2", width="30", bg=pestas_color, command = info).pack()
	ventana_agregar.title("Agregar")
	
	ventana_agregar.geometry("400x250")

def info():	
	nos_info = nos.get()
	codigo1_info =codigo1.get()
	cantidad_info =cantidad.get()

	print(nos_info, "\t", codigo1_info, "\t", cantidad_info)

file = open("agregar.txt", "a")
  file.write(nos_info)
  file.write("\t")
  file.write(codigo1_info)
  file.write("\t")
  file.write(cantidad_info)
  file.write("\t")


ventana_inicio()
