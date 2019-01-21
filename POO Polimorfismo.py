class Coche():

	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

class Moto():

	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")

class Camion():

	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")


def despalzamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Camion()
despalzamientoVehiculo(miVehiculo)

#miVehiculo=Moto()
#miVehiculo.desplazamiento()

#miVehiculo2=Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3=Camion()
#miVehiculo3.desplazamiento()
