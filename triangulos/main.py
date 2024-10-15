import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from opmat import OpMat
from triangulo import Triangulo

def Axis():
    glColor3f(1.0, 0.0, 0.0) 
    glBegin(GL_LINES)
    glVertex2f(-500, 0)
    glVertex2f(500, 0)
    glEnd()
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(0, -500)
    glVertex2f(0, 500)
    glEnd()

def main():
    pygame.init() 
    screen = pygame.display.set_mode((900, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Triangulos Fany") 

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-450, 450, -300, 300)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0, 0, 0, 0) 
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  
    glShadeModel(GL_FLAT)

    opmat1 = OpMat()
    triangle1 = Triangulo(opmat1)

    angle1 = 0
    angle2 = 0
    angle3 = 0

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        glClear(GL_COLOR_BUFFER_BIT) 
        Axis()

        #Triangulo Sol
        opmat1.push()
        opmat1.rotate(angle1) 
        opmat1.scale(30,30)
        glColor3f(1.0, 0.0, 0.0)  
        triangle1.Draw(opmat1)
        opmat1.pop()

        # Triangulo Tierra
        opmat1.push()
        opmat1.rotate(angle2) 
        opmat1.translate(100, 100) 
        opmat1.push()
        opmat1.scale(25,25)
        glColor3f(0.0, 1.0, 0.0)
        triangle1.Draw(opmat1)

        #Triangulo Luna
        opmat1.pop()
        opmat1.push()
        opmat1.rotate(angle3) 
        opmat1.translate(50, 50) 
        opmat1.scale(10,10)
        glColor3f(0.0, 0.0, 1.0)
        triangle1.Draw(opmat1)
        opmat1.pop()
        opmat1.pop()

        angle1 += 1
        angle2 += 4
        angle3 += 3

        if angle1 > 360:
            angle1 = 0
        if angle2 > 360:
            angle2 = 0
        if angle3 > 360:
            angle3 = 0

        pygame.display.flip() 
        pygame.time.wait(30)

    pygame.quit()

if __name__ == "__main__":
    main()