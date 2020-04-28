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

#Funcion que dibuja una hoja
def hoja(t,a):
	# El valor "t" indica el tamaño del radio de los semicirculos que se generaran
	# El valor "a" indica el angulo en que los semicurculos se uniran
	# Mientras mas cerrado sea "a", la hoja tendra un apariencia mas alargada
	turtle.color("Green") # Cambia de color a verde
	turtle.begin_fill()# Comienza relleno
	turtle.right(a/2)#gira a la derecha con a/2 grados
	turtle.circle(t,a)#dibuja un circulo de radio "t" y con angulo "a"
	turtle.left(180-a)#gira a la izquierda 180-a grados
	turtle.circle(t,a)#dibuja un circulo de radio "t" y angulo "a"
	turtle.left(180-a/2)#gira a la izquierda 180-a/2 grados
	turtle.end_fill()# Termina de rellenar
	turtle.color("Black")# Cambia de color a negro

ANG = 20
RAND = 10
REL = 2/3
RANDT = 60
GROSORTRONCO = 2
TAMINIC = 150
TAMHOJA = 10
ANGHOJA = 60
PROF = 10


def arbol(t, d):
	if d==0:
		turtle.forward(t)
		hoja(TAMHOJA, ANGHOJA)
		turtle.penup()
		turtle.back(t)
		turtle.pendown()
		return
	else:
		angulo1 = ANG + random.randrange(-RAND, RAND+1)
		angulo2 = ANG + random.randrange(-RAND, RAND+1)
		tamano = t + t * random.randrange(-RANDT, RANDT+1)/100
		turtle.pensize(d+GROSORTRONCO)
		turtle.forward(tamano)
		arbol(t*REL, d-1)
		turtle.left(angulo2)
		turtle.penup()
		turtle.back(tamano)
		turtle.pendown()
	

	
#Baja el centro del lapiz sin dibujar nada
turtle.penup()
turtle.right(90)
turtle.forward(300)
turtle.right(270)
turtle.pendown()

#Dibuja
turtle.speed(0)
turtle.left(90)
arbol(150, 8)
turtle.done()