import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
sys.path.append('..')
from OpMat import OpMat
from Piramide import Piramide

import math
import numpy as np

op3D = OpMat()
op3D.loadId()
objeto1 = Piramide(op3D)

pygame.init()

screen_width = 900
screen_height = 600

# Variables de cámara
FOVY = 60.0
ZNEAR = 1.0
ZFAR = 500.0

# Posición del observador
EYE_X = 10.0
EYE_Y = 10.0
EYE_Z = 10.0
CENTER_X = 0
CENTER_Y = 0
CENTER_Z = 0
UP_X = 0
UP_Y = 1
UP_Z = 0

# Variables para dibujar los ejes del sistema
X_MIN = -500
X_MAX = 500
Y_MIN = -500
Y_MAX = 500
Z_MIN = -500
Z_MAX = 500

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    
    # Eje X en rojo
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN, 0.0, 0.0)
    glVertex3f(X_MAX, 0.0, 0.0)
    glEnd()
    
    # Eje Y en verde
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, Y_MIN, 0.0)
    glVertex3f(0.0, Y_MAX, 0.0)
    glEnd()
    
    # Eje Z en azul
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, Z_MIN)
    glVertex3f(0.0, 0.0, Z_MAX)
    glEnd()
    glLineWidth(1.0)

def draw_path(a=5.0, num_points=1000):
    glColor3f(1.0, 1.0, 0.0)  
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    
    # Genera puntos 
    for i in range(num_points + 1):
        # Calcula el ángulo para el punto actual
        angle = (i / num_points) * 2 * math.pi 
        t = angle
        
        # Paramétrico
        # Ecuacionespara calcular las coordenadas X y Z
        denom = math.sin(t)**2 + 1  # Denominador de las ecuaciones, siempre positivo
        if denom == 0:
            denom = 0.0001  # No división entre 0
        
        # Calcula la coordenada X
        x = (a * math.sqrt(2) * math.cos(t)) / denom
        # Calcula la coordenada 
        z = (a * math.sqrt(2) * math.cos(t) * math.sin(t)) / denom
        y = 0.0  
        
        glVertex3f(x, y, z)

    glEnd()
    glLineWidth(1.0)


def Init():
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: Ejes 3D")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width / screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X, CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

Init()

done = False

def display1():
    objeto1.render()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Axis()
    draw_path(a=5.0, num_points=1000)  # Dibujar infinitow
    objeto1.update()
    display1()
    pygame.display.flip()
    pygame.time.wait(20) 

pygame.quit()
