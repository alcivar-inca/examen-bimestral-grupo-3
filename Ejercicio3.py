
def archivo():

	archi=open('texto.txt','r')
	texto=archi.readline()
	contador=0
	while texto!="":
		cont=texto.split(".")
		for i in range(len(cont)):
			palabras=len(cont[i].split(" "))
			contador=contador+1
			print (str(palabras) +" palabras")
			print (str(contador))
			texto=archi.readline()


archivo()
	

