# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import math
import random as rdn
import numpy as np

### Algorithm ###

def set_pixel(x, y, r, g, b, size):
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
	# print("{}\t{}".format(x, y))

def color_pixel(width, height, x, y, size):
	rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size , 
						GL_RGB, GL_UNSIGNED_BYTE, None)
	return list(rgb)

def DDA(x0, y0, x1, y1, r, g, b, size):
	points = []
	dx = x1 - x0
	dy = y1 - y0

	x = x0
	y = y0

	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)

	xi = dx / steps
	yi = dy / steps

	set_pixel(round(x), round(y), r, g, b, size)
	points.append((round(x), round(y)))
	for k in range(int(steps)):
		x += xi
		y += yi
		set_pixel(round(x), round(y), r, g, b, size)
		points.append((round(x), round(y)))
	return points

def Circle8v(xc, yc, radio, r, g, b, size):

	for x in range(math.ceil(radio / math.sqrt(2)) + 1):
		y = math.ceil(math.sqrt(radio * radio - x * x))
		set_pixel(xc + x, yc + y, r, g, b, size)
		set_pixel(xc - x, yc + y, r, g, b, size)
		set_pixel(xc - x, yc - y, r, g, b, size)
		set_pixel(xc + x, yc - y, r, g, b, size)

		set_pixel(xc + y, yc + x, r, g, b, size)
		set_pixel(xc - y, yc + x, r, g, b, size)
		set_pixel(xc - y, yc - x, r, g, b, size)
		set_pixel(xc + y, yc - x, r, g, b, size)

def DrawPolygon(vertices, r, g, b, size):
	# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
	vertices.append(vertices[0])
	for k in range(len(vertices) - 1):
		x0, y0 = vertices[k]
		x1, y1 = vertices[k + 1]
		DDA(x0, y0, x1, y1, r, g, b, size)


### Draw
def display_openGL(width, height, scale):
	pygame.display.set_mode((width, height), pygame.OPENGL)

	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	# glScalef(scale, scale, 0)

	gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)



def MoveDefender(x, y, sx, sy):
	set_pixel( x, y, 0/255, 0/255, 0/255, 50)

	if( sx == 50 ):
		if( (abs(y)%100 == 50) and ( x < 450) ):
			x = x + sx
	if( sx == -50 ):
		if( (abs(y)%100 == 50) and ( x > -450) ):
			x = x + sx
	if( sy == 50 ):
		if( (abs(x)%100 == 50) and ( y < 250) ):
			y = y + sy
	if( sy == -50 ):
		if( (abs(x)%100 == 50) and ( y > -250) ):
			y = y + sy
	return x, y
