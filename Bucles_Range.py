for i in range(5,50,3): # Aqui el 5 es el valor donde comienza el conteo, el 50 es el límite
# -y el 3 es de cuanto en cuanto se irá contando
	print(f"valor de la variable {i}")
	#en donde f"texto{variable}" está uniendo texto con el valor de una variable

valido=False

email=input('Introduce tu email: ')

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido==True:
	print("email correcto")
else:
	print("email incorrecto")

# Efectivamente range solo funciona con un valor numérico dentro de sus paréntesis, por lo que,
# -el valor de input al ser texto, hay que convertirlo con len(), en el ejemplo se muestra
# -que email tiene un len de 4, pero al agregarlo al if no sería solo if i, sino if email[i]