'''
PIA Programacion basica
Semana 2, funcion 3: Estructuracion de datos
Responsables: Orlando Sánchez Rivera, Francisco Sebastián Barrrientos Jiménez
Descripcion: calcula el promedio de los paises y escribe una lista de entradas en un archivo con las siguientes entradas: El nombre del pais, El PIB Promedio, Una lista de los PIBs, y la fecha obtenida de cada PIB
'''
def estructuracion(dic):
	nombres=[]
	proms=[]
	pibs=[]
	fechas=[]

	for pais,v in dic.items():
		temppib=[]
		tempfech=[]
		suma=0
		for fech,pib in v.items():
			temppib+=[pib]
			suma+=pib
			tempfech+=[int(fech)]
		suma/=len(v.values())
		
		pibs.append(temppib)
		fechas.append(tempfech)
		nombres+=[pais]
		proms+=[suma]
	
	with open("estructura.txt","w") as arch:
		arch.write("Fechas"+str(fechas)+"\n")
		for i in range(len(nombres)):
			arch.write("'"+nombres[i]+"',"+str(proms[i])+","+str(pibs[i])+"\n")