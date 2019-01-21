for letra in "Python":
	
	if letra== "h":
		continue

	print("Viendo la letra " + letra)

# Aqui podemos destacar que la función de continue es saltar el comando print de la letra h 

nombre="Pildoras Informáticas"

contador=0

for i in nombre:
	
	if i==" ":
		continue
	contador+=1

print(contador)

# Esta gestión se realiza para contar solamente los caracteres sin tomar los espacios

#while True:
#	pass 

# Queda funcionando hasta que el usuario presione Cntrl C

class MiClase:
	pass 

# Se deja la clase para mas tarde, se omite

email=input("Introcude tu email, por favor: ")

for i in email:
	
	if i=="@":
		arroba=True

		break;

else:
	arroba=False

print(arroba)

# El else solo se activará en caso de que todo el bucle haya sido recorrido con normalidad, es decir
# Que el i haya sido = a todos los caracteres ingresados