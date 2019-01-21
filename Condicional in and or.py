edad=18

if 0<edad<100:
	print("La edad es correcta")

else:
	print("Edad incorrecta")

#Se agrega ates de la variable en if otro operador de comparación

salario_presidente=int(input("Introduce el salario del presidente: "))
print("El salario del presidente es: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("El salario del director es: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del Jefe de Área: "))
print("El salario del Jefe de Área es: " + str(salario_jefe_area))

salario_administracion=int(input("Introduce el salario del Área administrativa: "))
print("El salario del Área administrativa es: " + str(salario_administracion))

if salario_presidente>salario_director>salario_jefe_area>salario_administracion:
	print("Todo funciona correctamente")

else:
	print("Algo falla en esta empresa")

# Se utiliza en muchas variables
