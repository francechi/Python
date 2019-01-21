texto = (input("Por favor ingresa un Texto: "))
palabras = 0
a = 0
letras = 0
texto = " "+texto+" "

for i in range(len(texto)):
    if i > 0:
        if texto[i] == " " and texto[i-1] != " ":
            palabras += 1

    if i != (len(texto)-1):
        if texto[i] == " " and texto[i+1] == "a" or texto[i+1] == "A":
            a += 1

    if texto[i] != " ":
        letras += 1


print("Palabras: " + str(palabras))
print("Palabras con a: " + str(a))
print("Letras: " + str(letras))
