i=1

while i<=10:
	print('Ejecución ' + str(i))
	i=i+1

print('Terminó la Ejecución')

# While = mientras

edad=int(input("indroduce tu edad: "))

while edad<15 or edad>100:
	print("Has introducido una edad Incorrecta, Vuelve a intentarlo")
	edad=int(input("indroduce tu edad: "))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))

# Se ejecuta como una condicion if, la diferencia es que while es infinito mientras no se cumplan
# - los requisitos

import math

print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número: "))

intentos=0

while numero<0:
	print("No se pude hallar la raíz de un número negativo")

	if intentos== 2:
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break;

	numero=int(input("Introduce un número: "))
	if numero<0:
		intentos=intentos+ 1

if intentos<2:
	solucion=math.sqrt(numero) # Lo que hace esta clase maht.sqrt es almacenar la raiz cuadrada
# - de numero en una variable llamada solucion
# Por lo que al principio para poder usar la clase maht, es necesario importarla con import
	print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))

# Y break; es para terminar con el bucle while


