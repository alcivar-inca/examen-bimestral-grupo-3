import sys
import math
from tkinter import *

def calcular():
	try:
		_valor = int(entrada_texto.get())
		#_valor = _valor + 2
		area = 4 * math.pi * math.pow(_valor,2)
		volumen = (4/3)*math.pi*math.pow(_valor,3)
		etiqueta.config(text = area)
		etiqueta1.config(text = volumen)
	except ValueError:
		etiqueta.config(text = "Introduce un numero")

app = Tk()
app.title("Area y Volumen de la Esfera")

#Ventaja Principal
vp = Frame(app)
vp.grid(column = 0, row = 0, padx = (50,50), pady = (10,10))
vp.columnconfigure(0, weight = 1)
vp.rowconfigure(0, weight = 1)


etiqueta0 = Label(vp, text = "Area")
etiqueta0.grid(column=2, row=3, sticky=(W, E))

etiqueta = Label(vp, text = "valor")
etiqueta.grid(column=2, row=4, sticky=(W, E))

etiqueta2 = Label(vp, text = "Volumen")
etiqueta2.grid(column=3, row=3, sticky=(W, E))

etiqueta1 = Label(vp, text = "valor1")
etiqueta1.grid(column=3, row=4, sticky=(W, E))

boton = Button(vp, text = "CALCULAR!", command = calcular)
boton.grid(column = 2, row = 2)

etiqueta5 = Label(vp, text = "RADIO = ")
etiqueta5.grid(column=1, row=1, sticky=(W, E))

valor = ""
entrada_texto = Entry(vp, width = 10, textvariable = valor)
entrada_texto.grid(column = 2, row = 1)

app.mainloop()


