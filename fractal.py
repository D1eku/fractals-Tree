import turtle
import random

#Funcion que dibuja un arbol fractal recursivo, con profundidad prof y tamaño de dibujo tam
def arbolSimple(tam, prof):
	if prof == 0:#Si la profundida es 0
		hoja(10, 60)# dibuja una hoja
		return#Finaliza
	else:#Si la profundidad no es 0
		turtle.forward(tam)#Dibuja una linea de tamaño "tam"
		turtle.left(45)# gira a la izquierda 45 grados
		arbol(tam*2/3,prof-1)#llama a la funcion arbol, para dibujar un arbol de tamaño reducido, reduciendo en 1 la profundidad del arbol
		turtle.right(90)#gira a la derecha 90 grados
		arbol(tam*2/3,prof-1)#llama a la funcion arbol para dibujar un arbol de tamaño menor y profundidad menor
		turtle.left(45)#gira a la izquierda 45 grados
		turtle.back(tam)#dibuja una linea de tamaño tam

def variacionColor(color, var):
	# A la tupla de color 
	# Los hace variar en "var" %
	# Luego devuelve el valor nuevo de la tupla color.
	Rd = random.randrange(-var, var+1)
	Gd = random.randrange(-var, var+1)
	Bd = random.randrange(-var, var+1)
	
	R, G, B  = color
	
	R += Rd
	G += Gd
	B += Bd
	
	if R > 255:
		R = 255
	elif R < 0:
		R = 0
	if G > 255:
		G = 255
	elif G < 0:
		G = 0
	if B > 255:
		B = 255
	elif B < 0:
		B = 0
	return R, G, B

def randomColor():
	R = random.randint(0, 255)
	G = random.randint(0, 255)
	B = random.randint(0, 255)
	return R,G,B
	
#Funcion que dibuja una hoja
def hoja(t,a):
	# El valor "t" indica el tamaño del radio de los semicirculos que se generaran
	# El valor "a" indica el angulo en que los semicurculos se uniran
	# Mientras mas cerrado sea "a", la hoja tendra un apariencia mas alargada
	turtle.color(variacionColor(colorHojas, colorHojasVar))# Varia el color de las hojas
	turtle.begin_fill()# Comienza relleno
	turtle.right(a/2)#gira a la derecha con a/2 grados
	turtle.circle(t,a)#dibuja un circulo de radio "t" y con angulo "a"
	turtle.left(180-a)#gira a la izquierda 180-a grados
	turtle.circle(t,a)#dibuja un circulo de radio "t" y angulo "a"
	turtle.left(180-a/2)#gira a la izquierda 180-a/2 grados
	turtle.end_fill()# Termina de rellenar

def randomTree():
	Angulo = random.randint(0,45)
	r1 = random.randrange(1, 4)
	r2 = random.randint(5,9)
	relacionCrecimiento = r1/r2
	tamInit = random.randint(20,200)
	return Angulo, relacionCrecimiento, tamInit

def randomHoja():
	tamHoja = random.randint(1,15)
	anguloHoja = random.randint(10,180)
	return tamHoja, anguloHoja
#Variables de control de tamaño del dibujo del arbol

ANG = 45 #Angulo de rotacion basico de las ramas
RAND = 0 # Numero random de cambio del angulo de las ramas
REL = 2/3 # Proporcion para las nuevas ramas
RANDT = 20 # Porcentaje de cambio del tamaño entre cada rama
GROSORTRONCO = 2 #Grosor inicial del tronco
TAMINIC = 150 # Tamaño inicial del tronco
TAMHOJA = 5 # Tamaño de las hojas
ANGHOJA = 60 # Angulo de las hojas
PROF = 10 #Cantidad maxima de profundidad del arbol

#Variables de colores del arbol
colorTronco = (97,56,11) #Color del tronco
colorTroncoVar = 30 #Variacion de color del tronco
colorHojas = (10,190,80) #Color de las hojas
colorHojasVar = 100 #Variacion de color de las Hojas
colorFondo = (255,255,255) #Color del fondo


#Colores random

colorTronco = randomColor()#Genera un color random para el tronco
colorHojas = randomColor()#Genera un color random para las hojas

def arbol(t, d):
	if d==0:#Si la dimension en 0 
		turtle.forward(t) # Dibuja una linea de temañano "t"
		hoja(TAMHOJA, ANGHOJA)#Dibuja una hoja
		turtle.up()# levanta el lapiz 
		turtle.back(t)# vuelve hacia atras en "t" distancia
		turtle.pd()# baja el lapiz para volver a dibujar
		turtle.color(colorTronco)
		return#termina
	else:#Si la dimension es distinto de 0
		turtle.color(colorTronco)
		angulo1 = ANG + random.randrange(-RAND, RAND+1)#Obtiene unangulo1 generado random entre RAND
		angulo2 = ANG + random.randrange(-RAND, RAND+1)#Obtiene un angulo2 generado random entre RAND
		tamano = t + t * random.randrange(-RANDT, RANDT+1)/100#genera el tamaño o el largo a dibujar
		turtle.pensize(d+GROSORTRONCO)# define el tamaño del pincel
		turtle.forward(tamano)#dibuja una linea de tamaño "tamano"
		turtle.left(angulo1)#gira a la izquierda en "angulo1" grados
		arbol(t*REL, d-1)# dibuja un arbol nuevo con profundidad menor y con relacion al tamaño del arbol inicial
		turtle.right(angulo1+angulo2)#rota a la izquierda en "angulo1 + angulo2" grados
		arbol(t*REL, d-1)# dibuja un arbol nuevo con profundidad menor y con relacion al tamaño del arbol inicial
		turtle.left(angulo2)#gira a la izquierda en "angulo2" grados
		turtle.up()#levanta el lapiz
		turtle.back(tamano)# vuelve hacia atras en "t" distancia
		turtle.pd()#baja el lapiz
	


#Dibuja
turtle.up()
turtle.right(90)
turtle.forward(200)
turtle.right(270)
turtle.down()

turtle.hideturtle()
turtle.colormode(255)
turtle.speed(0)#Define la velocidad de dibujado en maxima velocidad
turtle.left(90)#Gira a la izquierda en 90 grados
turtle.color("Brown")
arbol(TAMINIC, PROF)#Dibuja un arbol de tamaño "TAMINIC" y profundidad "PROF"
turtle.done()#Espera el cierre