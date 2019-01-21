class Vehiculos():

	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
		

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, 
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena) # \n Salto de línea


class Moto(Vehiculos):

	caballito="Hola"

	def caballito(self):
		self.caballito="Voy haciendo el caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, 
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.caballito)
		# En este caso estamos sobreescribiendo el método estado de la super clase Vehiculo
		#- copiando, pegando y modificando el código


class Furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta está cargada"

		else:
			return "La furgoneta no está cargada"
		
class VElectricos(Vehiculos):

	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True

class BicicletaElectrica(VElectricos,Vehiculos): # De ésta forma se realiza una herencia múltiple
	
	

	def luces(self, luces):
		self.luces=False
		if(self.luces):
			return "Luces Encendidas"

		else:
			return "Luces Apagadas"


miMoto=Moto("Honda", "CBR")

miMoto.caballito()
miMoto.estado() # Cuando es llamado miMoto.estado, se remplaza el estado de la super clase y 
				#- es traido el estado de la clase Moto ya modificado

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici=BicicletaElectrica("Nike", "CK300")
							# Se le da preferencia a los argumentos del constructor de la primera
							#- clase que se hereda, en este caso VElectricos, cuyo constructor
							#- no tiene argumentos.
miBici.arrancar()
miBici.estado()
print(miBici.luces(True))

# La herencia es una super clase que le otorga por defecto todos los valores de propiedades y
#- comportamientos, a todas las micro clases que deseen obtener éstos valores.


class Persona():

	def __init__(self, nombre, edad, lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	def descripcion(self):
		print("Nombre:", self.nombre, "Edad:", self.edad, "Residencia:", self.lugar_residencia)


class Empleado(Persona):

	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
		self.salario=salario
		self.antigüedad=antigüedad

	def descripcion(self):

		super().descripcion()
		print("Salario:", self.salario, "Antigüedad:", self.antigüedad)

manuel=Empleado(1500, 15, "Manuel", 55, "Colombia")

manuel.descripcion()
print(isinstance(manuel, Empleado))

# El principio de la sustitucion dice que una clase "es siempre un/a", en este caso un Empleado
#- es siempre una Persona, pero una persona no siempre es un empleado
# Se usa el insistance para verificar si un objeto pertenece(True) o no(False) a una clase.
# super() llama al método de la clase padre para que sea integrada a la clase actual.