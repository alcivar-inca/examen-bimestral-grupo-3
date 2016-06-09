from tkinter import *

def triangulos():
	x1=0; y1=30
	x2=20 ; y2=0
	x3=40

	ancho= 0
	alto=0
	ventana= Tk() # Creamos un objeto Tk
	ventana.title("Ejercicio 6") # Titulo de la ventana
	canvas = Canvas(ventana, width=400, height=400)
	canvas.pack()
	while alto<=360:
		while ancho <=360:
			canvas.create_polygon(x1,y1 ,x2,y2 ,x3,y1,fill= 'black')
			ventana.mainloop()

triangulos()