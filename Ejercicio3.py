

def archivo():

	archi=open('texto.txt','r')
	texto=archi.readline()
	contador=0
	palab=0
	while texto!="":
		cont=texto.split(".")
		for i in range(len(cont)):
			palabras=len(cont[i].split(" "))
			contador=contador+1
			palab=palab+palabras
			texto=archi.readline()
	print ("Existen "+str(contador+1)+" saltos de linea")
	print ("Existen "+str(palab) +" palabras")


archivo()
	