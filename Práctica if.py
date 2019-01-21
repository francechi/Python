print("Programa de evaluación de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion
	# >, <, ==, >=, <=, != (diferente que)

print(evaluacion(int(nota_alumno)))

# Es importante que cuando ingresemos el dato dentro de input, éste reconozca el tipo de valor 
# - en este caso es un valor numérico y se representa como int() colocado en print
