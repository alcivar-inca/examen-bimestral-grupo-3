#EJERCICIO 4
#-- Ingresar una palabra, traducir, 
#-- mostrar en pantalla y guardar en un archivo--

import goslate
from tkinter import *

from textblob import TextBlob

#Creamos el archivo
def creartxt():
	archivo = open('FrasesT.txt','w')
	archivo.close()

#Ingresamos una palabra
app = Tk()
app.title("Aplicacion grafica en python")
frase = input('Ingrese una palabra: ')
blob = TextBlob(frase)
#print(blob.translate(to="en"))

#Mostramso la palabra traducida en pantalla
palabra = blob.translate(to="en")
etiqueta = Label(app, text = palabra)

#Guardamos resultado
creartxt()
archivo = open('FrasesT.txt','w')
frase = archivo.write(str(palabra))
archivo.close()

etiqueta.pack()
app.mainloop()