#	EJERCICIO NUMERO 2

def ingresoDatos():
	resp =0 
	contador=1
	num=int(input("Ingrese un numero: "))
	archivo=open('texto1.txt', 'a')
	while resp< 1000:
		resp=num*contador
		print("Un multiplo es: "+ str(resp))
		archivo.write(str(resp) + "\n")
		contador= contador+1
	archivo.close()

ingresoDatos()