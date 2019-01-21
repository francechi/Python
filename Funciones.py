def mensaje(): # Declaración de la función

	print("Estamos aprendiento python") # Cuerpo de la función

mensaje() # Llamada a la función

# La función de la funcipon es reutilizar el código

def suma(num1, num2):
	
	print(num1+num2)

suma(3, 4)

suma(4, 5.343)

suma("Hola ", "¿Como estás?") # Sólo funciona con signo +

# Así se usan los parámetros

def suma2(num12, num22):
	
	resultado=num12+num22
	return resultado

suma2(3, 4)

print(suma2(4, 5.343)) # Aqui estariamos imprimiendo sólo ésta suma

suma2("Hola ", "¿Como estás?")

almacena_resultado=suma2(5, 8)

print(almacena_resultado)