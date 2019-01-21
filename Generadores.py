def generaPares(limite):

	num=1
	miLista=[]

	while num<limite:

		miLista.append(num*2)

		num+=1

	return miLista

print(generaPares(10))

# De esta forma estaríamos creando un sencilla función

def generaPares2(limite2):

	num2=1
	

	while num2<limite2:

		yield num2*2

		num2+=1

devuelvePares=generaPares2(10)

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

# Se usa el next para que de 1 a 1 se vayan imprimiendo los valores agregados en devuelvePares
# - causado por el yield, pues, éste funciona para ir reflejando 1 a 1

def devuelve_ciudades(*ciudades): # Lo que significa el * es que los valores que vamos a entregarle
#- a el/los parámetro(s) pueden ser demasiados (infinitos) y que a su vez sean guadados en tupla(s)
	for elemento in ciudades:
		#for subElemento in elemento:
			yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

# Lo que se refleja en el texto es que en vez de el yiel ir mostrando los valores asignados al
# - parámetro, muestre los subelementos dentro de ciudades.

print(next(ciudades_devueltas))