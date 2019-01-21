contraseña=input("Contraseña: ")
contador= 0

for i in contraseña:
	if i== " ":
		contador= contador * 0
	if i==i:
		contador= contador + 1

if contador>8 and contador<15:
	print("Contraseña OK")
else:
	print("Contraseña incorrecta")



email=input("Email: ")
contador1= 0
elpunto= False

for e in email:
	if e== "@":
		contador1= contador1 + 500
	if e== ".":
		elpunto= True
	if e==e:
		contador1= contador1 + 1

if contador1>500 and contador1<550 and elpunto== True:
	print("Email OK")
else:
	print("Email Incorrecto")


