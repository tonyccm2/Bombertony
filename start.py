
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *


from utils import *
from letras import *

def inicio():
    width= -60
    height= 0
    L_S(width,height,1)
    L_T(width+5,height,1)
    L_A(width+10,height,1)
    L_R(width+15,height,1)
    L_T(width+20,height,1)

def salida():
    b1=40
    b2=0
    L_E(b1,b2,1)
    L_X(b1+5,b2,1)
    L_I(b1+10,b2,1)
    L_T(b1+15,b2,1)

def marco(vertices):
    size=5
    r,g,b=1, 0.7, 1
    DrawPolygon(vertices, r, g, b, size)

def clearCanvas():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def Choose(sx,sy):
    vertices=[[-20,-10,1],
              [ 20,-10,1],
              [ 20, 10,1],
              [-20, 10,1]]
    marco(vertices)
    v=traslate(vertices,sx,sy)
    clearCanvas()
    marco(v)
    puntero(sx,sy-21)
    inicio()
    salida()

def start():
    scale = 1
    width, height = scale * 600, scale * 300

    pygame.init()
    pygame.display.set_caption('BomberTony')

    display_openGL(width, height, scale)

    pygame.mixer.music.load('Sonidos/musica2.mp3')
    pygame.mixer.music.play(100)
    marcador=-1
    inicio()
    salida()

    glFlush()
    pygame.display.flip()
    cicle=True

    while cicle==True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                cicle==False
                return
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    sx=-50
                    sy=0
                    Choose(sx,sy)
                    marcador=0
                    glFlush()
            
                elif event.key==pygame.K_RIGHT:
                    sx=50
                    sy=0
                    Choose(sx,sy)
                    marcador=1
                    glFlush()
        
                elif event.key==pygame.K_SPACE:
                    if marcador==0:
                        cicle=False
                    elif marcador==1:
                        cicle=False

    return marcador