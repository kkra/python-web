import random

VERSION = "0.1"

print """
	 _  _   
	| |/ |  ___   ___  __  __
	|   <  / -_) |   ) \ \/ /
	|_|\_| \__\_ | | |  \  /
	                    /_/   v%s
-- https://github.com/kenyk7 --
""" % VERSION

continuar = 1
name = raw_input("Ingresa un nombre para jugar 21: ")

while continuar == 1:
	# print "Jugar 21"
	# dif = int(input("Elija la dificultad: "))
	# if dif == 1:
	# 	ndig = 2
	# else:
	# 	ndig = 4
	tope = 21

	num = ("1","2","3","4","5","6","7","8","9","10","As")
	tipos = ("Corazones","Espadas","Oros","Flores")
	# carta = ''
	# def nueva():
	cartaj = random.choice(num)
	tipoj = random.choice(tipos)
	pcartaj = cartaj + tipoj
	print "Carta de mano es: ", cartaj , " de ", tipoj
	pedir = raw_input("Pedir carta <s=si n=no> ")
	if cartaj == "As":
		cartaj = 11

	if pedir == "s":
		nueva = "s"
		carta1 = int(cartaj)
		while nueva == "s":
			cartajn = random.choice(num)
			tipojn = random.choice(tipos)
			pcartajn = cartajn + tipojn

			while cartajn in pcartaj:
				cartajn = random.choice(num)
			while tipojn in pcartaj:
				tipojn = random.choice(tipos)
			# pcartajn = cartajn + tipojn
			if cartajn == "As":
				cartajn = 11

			total = int(carta1) + int(cartajn)
			# while total <= tope:
			
			suma = total + int(cartajn)
			if suma <= tope :
				# suma = int(cartaj)  + int(cartajn)
				pass
			if suma == tope:
				print "Ganaste tienes 21 :)"
			elif suma > tope:
				print "Eres un perdedor :("	
			print "La nueva carta es : ", cartajn , " de ", tipojn, " y suman ", suma
			nueva = raw_input("Pedir otra: <s=si n=no>")

	cod = ''

	# for i in range(ndig):
	# 	eleg = random.choice(dig)
	# 	while eleg in cod:
	# 		eleg = random.choice(dig)
	# 	cod = cod + eleg

	# print "Codigo de ", ndig, "digitos"
	pro = input("Propon un codigo: ")
	intentos = 1
	# print (cod)
	while pro != cod:
		intentos = intentos + 1
		aciertos = 0
		coincidencias = 0
		for i in range(ndig):
			if pro[i] == cod[i]:
				aciertos = aciertos + 1
			elif pro[i] in cod:
				coincidencias = coincidencias + 1
		print "Tu Propuesta es :", pro, ", tienes ", aciertos, " aciertos y",\
			coincidencias, " coincidencias"
		pro = input("Propon otro codigo: ")
	print "Felicidades, lo lograste en ", intentos, "intentos"
	continuar = int(input("Seguir jugando? 1=si y 0=no "))