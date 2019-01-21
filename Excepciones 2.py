def divide():

	try: # try no puede estar sin except y sin finally

		op1=(float(input("Introduce el primer número: ")))

		op2=(float(input("Introduce el segundo número: ")))

		print("La división es: " + str(op1/op2))

	except:
		#print("Ha ocurrido un error") esto es para que con cualquier error slga éste mensaje sin
		#- especificar, y siga el proceso del programa

	except ValueError:

		print("El valor introducido es erróneo")

	except ZeroDivisionError:

		print("No se puede dividir entre 0!")

	finally: # Siempre se ejecutará éste código

		print("Cálculo finalizado")

divide()  

# Aqui se muestra como agragar varias excepciones en conjunto