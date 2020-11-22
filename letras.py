from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import math
import random as rdn
import numpy as np

def set_pixel(x, y, r, g, b, scale):
	glColor3f(r, g, b)
	glPointSize(scale)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()

def puntaje(ptj,x,y):
    if(ptj == 0):
        L_C(x,y)
        L_0(x,y)
    if(ptj == 1):
        L_C(x,y)
        L_1(x,y)
    if(ptj == 2):
        L_C(x,y)
        L_2(x,y)
    if(ptj == 3):
        L_C(x,y)
        L_3(x,y)
    if(ptj == 4):
        L_C(x,y)
        L_4(x,y)
    if(ptj == 5):
        L_C(x,y)
        L_5(x,y)
    if(ptj == 6):
        L_C(x,y)
        L_6(x,y)
    if(ptj == 7):
        L_C(x,y)
        L_7(x,y)
    if(ptj == 8):
        L_C(x,y)
        L_8(x,y)
    if(ptj == 9):
        L_C(x,y)
        L_9(x,y)


def L_0(x,y):
    R=[[0,0,1,1,1,1,1,1,1,0,0],
       [0,1,1,1,1,1,1,1,1,1,0],
       [1,1,1,0,0,0,0,0,1,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,1,0,0,0,0,0,1,1,1],
       [0,1,1,1,1,1,1,1,1,1,0],
       [0,0,1,1,1,1,1,1,1,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)

def L_1(x,y):
    R=[[0,0,0,0,1,1,1,0,0,0,0],
       [0,0,0,1,1,1,1,0,0,0,0],
       [0,0,1,1,1,1,1,0,0,0,0],
       [0,1,1,1,0,1,1,0,0,0,0],
       [0,1,1,0,0,1,1,0,0,0,0],
       [0,0,0,0,0,1,1,0,0,0,0],
       [0,0,0,0,0,1,1,0,0,0,0],
       [0,0,0,0,0,1,1,0,0,0,0],
       [0,0,0,0,0,1,1,0,0,0,0],
       [0,1,1,1,1,1,1,1,1,1,1],
       [0,1,1,1,1,1,1,1,1,1,1]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)
def L_2(x,y):
    R=[[0,0,0,1,1,1,1,1,0,0,0],
       [0,0,1,1,1,1,1,1,1,0,0],
       [0,1,1,1,0,0,0,0,1,1,0],
       [0,1,1,0,0,0,0,1,1,1,0],
       [0,0,0,0,0,0,1,1,1,0,0],
       [0,0,0,0,0,1,1,1,0,0,0],
       [0,0,0,0,1,1,1,0,0,0,0],
       [0,0,0,1,1,1,0,0,0,0,0],
       [0,0,1,1,1,0,0,0,0,0,0],
       [0,1,1,1,1,1,1,1,1,1,1],
       [0,1,1,1,1,1,1,1,1,1,1]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)
def L_3(x,y):
    R=[[1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [0,0,0,0,0,0,0,0,0,1,1],
       [0,0,0,0,0,0,0,0,0,1,1],
       [0,0,0,0,1,1,1,1,1,1,1],
       [0,0,0,0,1,1,1,1,1,1,0],
       [0,0,0,0,1,1,1,1,1,1,1],
       [0,0,0,0,0,0,0,0,0,1,1],
       [0,0,0,0,0,0,0,0,0,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)
def L_4(x,y):
    R=[[1,1,1,0,0,0,0,0,1,1,1],
       [1,1,1,0,0,0,0,0,1,1,1],
       [1,1,1,0,0,0,0,0,1,1,1],
       [1,1,1,0,0,0,0,0,1,1,1],
       [1,1,1,0,0,0,0,0,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [0,0,0,0,0,0,0,0,1,1,1],
       [0,0,0,0,0,0,0,0,1,1,1],
       [0,0,0,0,0,0,0,0,1,1,1],
       [0,0,0,0,0,0,0,0,1,1,1]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)
def L_5(x,y):
    R=[[1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,0,0,0,0,0,0,0,0,0],
       [1,1,0,0,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,0,0],
       [1,1,1,1,1,1,1,1,1,1,0],
       [0,0,0,0,0,0,0,0,1,1,1],
       [0,0,0,0,0,0,0,0,0,1,1],
       [1,1,0,0,0,0,0,0,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,0],
       [0,1,1,1,1,1,1,1,1,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)
def L_6(x,y):
    R=[[0,0,1,1,1,1,1,1,1,1,1],
       [0,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,0,0,0,0,0,0,0,0],
       [1,1,0,0,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,0,0],
       [1,1,1,1,1,1,1,1,1,1,0],
       [1,1,1,0,0,0,0,0,1,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,1,0,0,0,0,0,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,0],
       [0,1,1,1,1,1,1,1,1,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)
def L_7(x,y):
    R=[[1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [0,0,0,0,0,0,0,0,1,1,1],
       [0,0,0,0,0,0,0,1,1,1,0],
       [0,0,0,0,0,0,1,1,1,0,0],
       [0,0,1,1,1,1,1,1,1,1,0],
       [0,0,1,1,1,1,1,1,1,1,0],
       [0,0,0,1,1,1,0,0,0,0,0],
       [0,0,1,1,1,0,0,0,0,0,0],
       [0,1,1,1,0,0,0,0,0,0,0],
       [1,1,1,0,0,0,0,0,0,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)
def L_8(x,y):
    R=[[0,1,1,1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [0,1,1,1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [0,1,1,1,1,1,1,1,1,1,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)
def L_9(x,y):
    R=[[0,0,1,1,1,1,1,1,1,0,0],
       [0,1,1,1,1,1,1,1,1,1,0],
       [1,1,1,0,0,0,0,0,1,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,1,1,0,0,0,0,0,1,1,1],
       [0,1,1,1,1,1,1,1,1,1,1],
       [0,0,1,1,1,1,1,1,1,1,1],
       [0,0,0,0,0,0,0,0,0,1,1],
       [0,0,0,0,0,0,0,0,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,0],
       [0,1,1,1,1,1,1,1,1,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, 1)

def L_C(x,y):
    R=[[0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==0: 
                set_pixel(x+j,y-i, 0, 0, 0, 1)
                