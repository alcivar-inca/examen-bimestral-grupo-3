#secuencia de los numeros primos desde 1 hasta el numero ingresado

numero= int (input ("Ingresar un numero entero, por favor:"))

def verificar_primo(numero):
	contador=0
	i=1
	while i<numero:
		if numero%i==0:
			contador=contador+1
		i=i+1
	return contador

def crearlista(numero):
	lista =[]
	i=2
	while i<=numero:
		lista.append(i)
		i=i+1
	return lista

def cprimo(lista):
	primos=[]
	for numero in lista:
		verificado=verificar_primo(numero)
		if verificado==2:
			primos.append(numero)
	return primos

lista=crearlista(numero)
primos=cprimo(lista)

print ("los numeros entre 1 y",numero,"son:",primos)

def creartxt():
	archivo = open('Numerosprimos.txt','w')
	archivo.close()

def grabartxt():
	archivo = open('Numerosprimos.txt','w')
	Numerosprimos= archivo.write(str(lista))
	
	archivo.close()

creartxt()
grabartxt()

#def leertxt():
#	archivo = open('Frases.txt','r')
#	linea = archivo.readline()
#	while linea!="":
#		print (linea)
#		print (len(linea.split(' ')))
#		linea=archivo.readline()
#	archivo.close()

#leertxt()


	

