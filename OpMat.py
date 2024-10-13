# Class OpMat
# init, translate, scale, rotate, print_T, print_E, print_R, print_A, matriz de nodelado, pila, funcion para multiplciar la matriz de modelado con lo spoligonos
# Triangulo:  definicion, Draw
# main: abrir OpenGl,  etc
# Tres triangulos, que giren como sistema solar, con rotacion, traslacion 

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

screen_width = 900
screen_height = 600

def LineaBresenham(x1, x2, y1, y2):
    dY = y2 - y1
    dX = x2 - x1

    IncXi = 1 if dX >= 0 else -1
    IncYi = 1 if dY >= 0 else -1
    dX = abs(dX)
    dY = abs(dY)

    if dX >= dY:
        IncYr = 0
        IncXr = IncXi
        avR = 2 * dY
        av = avR - dX
        avI = av - dX
    else:
        IncXr = 0
        IncYr = IncYi
        dX, dY = dY, dX
        avR = 2 * dY
        av = avR - dX
        avI = av - dX

    x = x1
    y = y1

    glBegin(GL_POINTS)
    while x != x2 or y != y2:
        glVertex2f(x, y)
        if av >= 0:
            x += IncXi
            y += IncYi
            av += avI
        else:
            x += IncXr
            y += IncYr
            av += avR
    glVertex2f(x2, y2)
    glEnd()

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
    screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Sistema Solar con Triángulos")
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-450, 450, -300, 300)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0, 0, 0, 0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glShadeModel(GL_FLAT)
    
    # Crear instancias de OpMat para cada triángulo
    opmat1 = OpMat()
    opmat2 = OpMat()
    opmat3 = OpMat()

    # Definir los triángulos
    triangle1 = Triangulo([(-30, -30), (30, -30), (0, 60)])
    triangle2 = Triangulo([(-20, -20), (20, -20), (0, 40)])
    triangle3 = Triangulo([(-10, -10), (10, -10), (0, 20)])

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

        # Triángulo 1 (el "sol", centro)
        opmat1.push()
        opmat1.rotate(angle1)
        glColor3f(1.0, 0.0, 0.0)
        triangle1.Draw(opmat1)
        opmat1.pop()

        # Triángulo 2 (primera órbita)
        opmat2.push()
        opmat2.translate(150, 0)
        opmat2.rotate(angle2)
        glColor3f(0.0, 1.0, 0.0)
        triangle2.Draw(opmat2)
        opmat2.pop()

        # Triángulo 3 (segunda órbita)
        opmat3.push()
        opmat3.translate(-200, -150)
        opmat3.rotate(angle3)
        glColor3f(0.0, 0.0, 1.0)
        triangle3.Draw(opmat3)
        opmat3.pop()

        # Incrementar ángulos para rotación
        angle1 += 1
        angle2 += 2
        angle3 += 3

        pygame.display.flip()
        pygame.time.wait(30)

    pygame.quit()

if __name__ == "__main__":
    main()
