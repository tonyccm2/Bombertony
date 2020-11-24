# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from utils import *
from letras import *
from start import *
from pygame.locals import *
import numpy as fsa
import threading


scale = 1 
""" no cambiar la escala de 1 """
width, height = scale * 1200, scale * 600

def bomba(xc, yc):
	Circle8v(xc, yc, 15, 0/255, 0/255, 0/255, 1)
	for k in range(1,15):
		Circle8v(xc, yc, k, 100/255, 100/255, 100/255, 1)
	DDA(xc+8, yc+8, xc+14, yc+14, 255/255, 200/255, 0/255, 3)
	set_pixel( xc+14,yc+14,255/255, 0/255, 0/255, 4)

	
def explocion(xc, yc, datos):
	posx=xc%100
	posy=yc%100
	if(posx == 50 or posx == -50):
		DDA(xc,250,xc,-250, 255/255, 100/255, 0/255, 40)
	
	if(posy == 50 or posy == -50):
		DDA(-450,yc,450,yc, 255/255, 100/255, 0/255, 40)

	set_pixel( xc,yc,255/255, 0/255, 0/255, 4)

	sonidoBoom = pygame.mixer.Sound("Sonidos/boom2.wav")
	sonidoBoom.play()

	glFlush()
	pygame.time.wait(100)
	R=False
	V=False
	if(xc == datos[0][0] or yc == datos[0][1]):
		if (xc == datos[0][0] and yc == datos[0][1]):
			R=True
		else:
			if(xc == datos[0][0] and abs(posx) == 50):
				R=True
			if(yc == datos[0][1] and abs(posy) == 50):
				R=True
	if(xc == datos[1][0] or yc == datos[1][1]):
		if (xc == datos[1][0] and yc == datos[1][1]):
			V=True
		else:
			if(xc == datos[1][0] and abs(posx) == 50):
				V=True
			if(yc == datos[1][1] and abs(posy) == 50):
				V=True
	if(R or V):
		if(R and V):
			print("no winner")
		else:
			if(V):
				print("win red")
				datos[4][0]+=1
			if(R):
				print("win green")
				datos[4][1]+=1
		pygame.time.wait(2000)
		return True
		
	return False
def limpiar_explo(xc, yc):
	posx=xc%100
	posy=yc%100
	if(posx == 50 or posx == -50):
		DDA(xc,250,xc,-250, 0/255, 0/255, 0/255, 40)
	
	if(posy == 50 or posy == -50):
		DDA(-450,yc,450,yc, 0/255, 0/255, 0/255, 40)


def mapa():
	#bordes
	x=487.5
	y=287.5

	vertices = [(-x, -y,1), (-x, y,1), (x, y,1), (x, -y,1)]
	DrawPolygon(vertices, 175/255, 175/255, 175/255, 25)
	x = -400
	for k in range(0,9):
		y = 200
		for l in range(0,5):
			set_pixel(-400+(k*100),200-(l*100),175/255, 175/255, 175/255, 50)


def Refresh(datos):
	personajeRojo(datos[0][0],datos[0][1])
	personajeVerde(datos[1][0],datos[1][1])
	bomba(datos[2][0],datos[2][1])
	bomba(datos[3][0],datos[3][1])
	puntaje(datos[4][0],-550,200)
	puntaje(datos[4][1], 550,200)
	glFlush()

def IniciarJuego():
	datos = [
		[-450, 250],#personaje rojo
		[ 450,-250],#personade verde
		[1000,1000],#bomba rojo
		[1000,1000],#bomba verde
		[0	 ,	 0],#puntos
	]

	mapa()
	personajeRojo(-550,250)
	personajeVerde(550,250)
	personajeRojo(datos[0][0],datos[0][1])
	personajeVerde(datos[1][0],datos[1][1])
	pygame.mixer.music.load('Sonidos/musica1.mp3')
	pygame.mixer.music.play(100)
	print("iniciado...")
	return datos

def Juego():
	
	pygame.init()
	pygame.display.set_caption('BomberTony')
	display_openGL(width, height, scale)

	datos = IniciarJuego()
	glFlush()
	pygame.display.flip()

	while True:
		if (datos[4][0] == 10):
			return "R"
		if (datos[4][1] == 10):
			return "G"
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT :
					sx = -50
					sy = 0
					datos[1][0], datos[1][1] = MoveDefender(datos[1][0], datos[1][1], sx, sy)
				elif event.key == pygame.K_RIGHT:
					sx = 50
					sy = 0
					datos[1][0], datos[1][1] = MoveDefender(datos[1][0], datos[1][1], sx, sy)
				elif event.key == pygame.K_UP :
					print("K_UP")
					sx = 0
					sy = 50
					datos[1][0], datos[1][1] = MoveDefender(datos[1][0], datos[1][1], sx, sy)
				elif event.key == pygame.K_DOWN :
					sx = 0
					sy = -50
					datos[1][0], datos[1][1] = MoveDefender(datos[1][0], datos[1][1], sx, sy)
				elif event.key == pygame.K_a :
					sx = -50
					sy = 0
					datos[0][0], datos[0][1] = MoveDefender(datos[0][0], datos[0][1], sx, sy)
				elif event.key == pygame.K_d:
					sx = 50
					sy = 0
					datos[0][0], datos[0][1] = MoveDefender(datos[0][0], datos[0][1], sx, sy)
				elif event.key == pygame.K_w :
					sx = 0
					sy = 50
					datos[0][0], datos[0][1] = MoveDefender(datos[0][0], datos[0][1], sx, sy)
				elif event.key == pygame.K_s :
					sx = 0
					sy = -50
					datos[0][0], datos[0][1] = MoveDefender(datos[0][0], datos[0][1], sx, sy)
				elif event.key == pygame.K_KP_ENTER :
					muerto=explocion( datos[3][0], datos[3][1] , datos)
					limpiar_explo( datos[3][0], datos[3][1] )
					datos[3][0]=datos[1][0]
					datos[3][1]=datos[1][1]
					if(muerto):
						print(muerto)
						set_pixel( datos[0][0], datos[0][1], 0/255, 0/255, 0/255, 50)
						set_pixel( datos[1][0], datos[1][1], 0/255, 0/255, 0/255, 50)
						datos = [
							[-450, 250],#personaje rojo
							[ 450,-250],#personade verde
							[1000,1000],#bomba rojo
							[1000,1000],#bomba verde
							[datos[4][0],datos[4][1]],#puntaje
						]
				elif event.key == pygame.K_f :
					muerto = explocion( datos[2][0], datos[2][1], datos)
					limpiar_explo( datos[2][0], datos[2][1] )
					datos[2][0]=datos[0][0]
					datos[2][1]=datos[0][1]
					if(muerto):
						set_pixel( datos[0][0], datos[0][1], 0/255, 0/255, 0/255, 50)
						set_pixel( datos[1][0], datos[1][1], 0/255, 0/255, 0/255, 50)
						datos = [
							[-450, 250],#personaje rojo
							[ 450,-250],#personade verde
							[1000,1000],#bomba rojo
							[1000,1000],#bomba verde
							[datos[4][0],datos[4][1]],#puntaje
						]
				Refresh(datos)

def hilo_start(name):
	global A 
	A = start()
	pygame.quit()
	sys.exit()
	
def hilo_game(name):
	global A
	if A==0:
		ganador = Juego()
	pygame.quit()
	sys.exit()
	

def main():
	global A 
	A = 0
	while(A==0):
		hilo1=threading.Thread(target=hilo_start,args=("hilo start",))
		hilo2=threading.Thread(target=hilo_game,args=("hilo juego",))
		hilo1.start()
		hilo1.join()
		hilo2.start()
		hilo2.join()


if __name__ == '__main__':
	main()
