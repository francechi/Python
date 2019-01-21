print("Verificación de acceso")

edad_usuario=int(input("Introduce tu edad: "))

if edad_usuario<18:
	print("No puedes pasar")

elif edad_usuario>120:
	print("Edad incorrecta")

else:
	print("Puedes pasar")

print("El programa ha finalizado")

# Es importante destacar que: Puede existir if sin else pero no puede existir else sin if
# - por otra parte, el else pertenece al if mas cercano, para esto, usamos el elif


print("Verificación de acceso")

nota_usuario=int(input("Introduce tu nota: "))

if nota_usuario<5:
	print("Raspao")

elif nota_usuario<6:
	print("De vaina")

elif nota_usuario<7:
	print("Ahí vamos")

elif nota_usuario<9:
	print("Eres un guebo pelao")

else:
	print("Machete!")

print("El programa ha finalizado")

# En este ejemplo usamos el elif para que todos los condicionales esten en bloque y funcione.