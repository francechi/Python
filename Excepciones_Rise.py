def evaluaEdad(edad):

	#if edad<0:
	#	raise TypeError("No se permiten edades negativas") # Puedes personalizar cualquier error

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "Estás con un pié aquí y otro allá"

print(evaluaEdad(-15))

# La función de raise es implantar un error y personalizar su mensaje
# Comenté la línea 3 y 4 para poder ejecutar el siguiente ejemplo

import math

def calculaRaiz(num1):

	if num1<0:
		raise ValueError("El número no puede ser negativo")

	else:
		return math.sqrt(num1)


op1=(int(input("Introduce un número: ")))

try:
	print(calculaRaiz(op1))

except ValueError as ErrorDeNumeroNegativo: # as se coloca para que el nombre que le demos al error
# - copie la descripción que tiene el error en raise

	print(ErrorDeNumeroNegativo) # sin el "as" tendríamos que colocar print("Cualquier mensaje")

print("Programa terminado")