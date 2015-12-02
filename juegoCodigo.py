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
while continuar == 1:
	print "Elija una dificultad 1=Facil  2=Dificil"
	dif = int(input("Elija la dificultad: "))
	if dif == 1:
		ndig = 2
	else:
		ndig = 4
	dig = ("0","1","2","3","4","5","6","7","8","9")
	cod = ''
	for i in range(ndig):
		eleg = random.choice(dig)
		while eleg in cod:
			eleg = random.choice(dig)
		cod = cod + eleg
	print "Codigo de ", ndig, "digitos"
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