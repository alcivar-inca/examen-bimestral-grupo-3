#	EJERCICIO NUMERO 5
# 	PROGRAMA QUE CALCULA EL AREA Y VOLUMEN DE UNA ESFERA DADO EL RADIO
import sys
from tkinter import *

def areaEsfera():
	area=0
	cadena=StringVar
	valor=0
	volumen=0

	def calculo():
		texto=""
		valor= int(texto.get())
		
		area=4*math.pi*math.pw(valor,2)
		volumen=(4/3)*math.pi*math.pow(valor,3)

		print("El area es: " + str(area))

	app=Tk()
	app.title("AREA DE UNA ESFERA")
	lamina1= Frame(app)
	lamina1 = Frame(app, height=200, width=400) # Creamos un frame en nuestro contenedor app
	lamina1.pack(padx=10, pady=10)
	label1=Label(lamina1, text ='Ingrese el radio de la esfera', font=(16)).place(x=0, y=0)
	texto= Entry(lamina1, width=20, font=("Arial", 16),textvariable=cadena).place(x=210, y=0)
	#label2=Label(lamina1, text ="El area es: " + str(area), font=(16)).place(x=210, y=35)
	#label3=Label(lamina1, text ="El volumen es: " + str(area), font=(16)).place(x=210, y=70)

	

	
	boton= Button(lamina1, width=10, text="Calcular", font=(16), command=calculo).place(x=0, y=35)


	app.mainloop()
areaEsfera()
