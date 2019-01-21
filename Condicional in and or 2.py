print('Programa de becas Año 2017')
distacia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distacia_escuela)

numero_hermanos=int(input("Introduce el número de hermanos del estudiante: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario anual bruto: "))
print(salario_familiar)

if distacia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a una Beca")

else:

	print("No tienes derecho a Beca")

# De esta forma se utiliza el and

print("Asignaturas Optativas Año 2017")
print("Informatica Gráfica - Pruebas de Software - Usabilidad y Accesibilidad")

opcion=input('Escriba la asignatura escogida: ')
asignatura=opcion.lower()

if asignatura in ("informatica gráfica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura " + asignatura, "tomada correctamente, a su email registrado le llegará un mensaje de horarios")

else:
	print("Asignatura Incorrecta, por favor seleccione una asignatura optativa")
 
print("Fin de programa")

# lower() transforma todo a minúscula y upper() transforma todo a mayúscula
# sin el lower solamente no se crea la variable opcion, si no, asignatura directamente
# Así se usa el condicional in