class Coche():

	def __init__(self): # Constructor # __init__ significa estado inicial (initial)

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 # los __ hacen que la propiedad no sea accesible fuera de la clase
		self.__enmarcha=False
		# con el __ estamos encapsulando las variables(propiedades)

	# Sin el constructor quedaba así:

	#largoChasis=250
	#anchoChasis=120
	#ruedas=4
	#enmarcha=False

	def arrancar(self,arrancamos): #self hace referencia a el propio objeto, instancia o ejemplar
	 #- de la clase 
	 #Un método (defs) es una función especial que pertenece a la clase donde se está creando(Coche)
	 #- mientras que una funcion no pertenece a una clase
		self.__enmarcha=arrancamos # Estamos creando esta variable para que dentro guarde el valor
		#- de arrancamos y así podamos utilizar ese valor

		if(self.__enmarcha):
			chequeo=self.__chequeo()

		if(self.__enmarcha==True and chequeo==True): # No colocar el True sería lo mismo
			return "El coche está en marcha"

		elif(self.__enmarcha and __chequeo==False):
			return "Algo ha ido mal en el chequeo, no podemos arrancar"

		else:
			return "El coche está parado"

	def estado(self):
		print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis,
			"y un largo de", self.__largoChasis)
		
	def __chequeo(self): # Aquí encapsulamos un método
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="Cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="Cerradas"):
			return True

		else:
			return False

		
print("---------------A continuación creamos el primer objeto----------------")
miCoche=Coche() #instanciar una clase - Crear objeto, instancia o ejemplar

print(miCoche.arrancar(True))
miCoche.estado()
#print(miCoche.__chequeo()) # No se ejecutará ésta llamada porque encapsulamos el método

print("---------------A continuación creamos el segundo objeto----------------")
miCoche2=Coche() #instanciar una clase - Crear objeto, instancia o ejemplar

print(miCoche2.arrancar(False))
miCoche2.ruedas=2 # Aquí estaríamos modificando una propiedad fuera de la clase # Pero no se está
#- modificando debido a que la propiedad ruedas está encapsulada con __
# Si se coloca miCoche2.__ruedas=2 daría el mismo resultado pero serpia ilógico escribirlo
miCoche2.estado()
#print(miCoche2.__chequeo())
# A la hora de programar con POO es habitual que las características comunes de los objetos 
#- formen parte de lo que se llama un estado inicial (de fábrica)

# Un constructor es un método especial ue le da estado inicial a los objetos

# Estamos encapsulando un método debido a que no tiene sentido que el coche realice un chequeo
#- con el auto apagado, pues al llamar al método print(miCoche.chequeo()) estaríamos
#- accediendo desde afuera de la clase. Por eso se junta dentro de def arrancar
#- incluimos la condicion para que tenga lógica.