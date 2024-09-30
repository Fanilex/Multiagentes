import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

pygame.init()

screen_width = 900
screen_height = 600

#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(X_MIN,0.0)
    glVertex2f(X_MAX,0.0)
    glEnd()
    #Y axis in green
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(0.0,Y_MIN)
    glVertex2f(0.0,Y_MAX)
    glEnd()
    glLineWidth(1.0)

def display():
    glColor3f(1.0, 0.0, 0.0)
    
    size = 1
    for i in range(10):
        glLineWidth(size)
        glBegin(GL_LINES)
        glVertex2i(-300,200-i*50)
        glVertex2i(300,200-i*50)
        glEnd()
        size += 1

def init():
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: ejes 2D")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-450,450,-300,300)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0,0,0,0)
    #OPCIONES: GL_LINE, GL_POINT, GL_FILL
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glShadeModel(GL_FLAT)

# código principal ---------------------------------
init()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT)
    Axis()
    #display()  
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()