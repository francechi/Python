midiccionario={"Alemania":"Berlin","Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)

# Para hacer un diccionario midiccionario={"":"",} o midiccionario={"":número,}
# Se agregan datos de la siguiente forma midiccionario["keys"]="values"
# - y se modifican de la misma manera o simplemente borras y remplazas
# - o mejor aún escribes el código correcto desde el principio
# midiccionario={"Alemania":"Berlin","Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"
#             ----------- "Italia"="Roma"} ------------


mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario2={mitupla[0]: "Madrid", mitupla[1]: "París", mitupla[2]: "Londres", mitupla[3]: "Berlín"}
print(midiccionario2["Francia"])

# De esta forma se llaman los elementos de la tupla creada hacia el diccionario
# - y al mismo tiempo se le agregan los valores desde el dicionario

midiccionario3={"Alemania":"Berlin", "Reino Unido":"Londres", "España":[1,2,3,54,84]}
print(midiccionario3["España"])

# Aquí se muestra una tupla ("España") dentro de un diccionario

midiccionario3={"Alemania":"Berlin", "Reino Unido":"Londres", "España":{"números":[1,2,3,54,84]}}
print(midiccionario3["España"])

# Aquí se muestra un diccionario ("España") dentro de un diccionario (midiccionario3) 
# - que a su vez tiene una tupla ("números")

print(midiccionario3.keys())
# Los .keys son los datos de la izquierda en el diccionario ("Alemania",)

print(midiccionario3.values())
# Los .values son los datos de la derecha en el diccionario ("Berlín",)

print(len(midiccionario3))
# El len(()) es la longitud del diccionario, es decir, el conjunto de .values y .keys que contiene 