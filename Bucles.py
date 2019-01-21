# Existen bucles Determinados e Indeterminados

for i in ["hola", "como", "estas", "chao"]:
	print(i)

# el bucle consiste en este caso, a la asignacion de cada valor a la variable i

for a in ["Píldoras", "Informáticas", 3]:
	print("Hola", end=" ")

# se usa end=" " para colocar en una sola línea todo el código

for b in "ivanfrancehi@hotmail.com":
	print("Chao", end=" ")

# imprime la palabra colocada las veces equivalentes al numero de caracteres del strings

email=False # Variable buleana

for c in "ivanfrancehi@hotmail.com":
	if(c=="@"): 
		email=True

if email==True: # Sería lo mismo dejar if email:
	print("El email es correcto")
else:
	print("El email es incorrecto")

# Como se va recorriendo cada caracter, en algun momento c será igual a @

email=False 
miEmail=input("Introduce tu direción de email: ")

for d in miEmail:
	if(d=="@"): 
		email=True

if email==True: 
	print("El email es correcto")
else:
	print("El email es incorrecto")

# Se le agrega el input


for f in range(5):
	print(f)

# rango