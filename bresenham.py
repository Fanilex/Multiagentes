import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

pygame.init()

screen_width = 900
screen_height = 600

X_MIN = -500
X_MAX = 500
Y_MIN = -500
Y_MAX = 500

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(X_MIN, 0.0)
    glVertex2f(X_MAX, 0.0)
    glEnd()
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, Y_MIN)
    glVertex2f(0.0, Y_MAX)
    glEnd()
    glLineWidth(1.0)
    
def LineaBresenham(x1, x2, y1, y2):
    # Diferenciales para comparar
    dY = y2 - y1
    dX = x2 - x1

    #SI el diferencial de DY es mayor o igual a 0
    if dY >= 0:
        IncYi = 1
    #SI el diferencial de DY es menor a 0
    else:
        dY = -dY
        IncYi = -1
    
    #SI el diferencia de DX es mayor o igual a 0
    if dX >= 0:
        IncXi = 1
    #SI el diferencial de DX es menor a 0
    else:
        dX = -dX
        IncXi = -1

    # Checo si el incremento es de lado o hacia arriba/de lado
    if dX >= dY:
        IncYr = 0
        IncXr = IncXi
    else:
        IncXr = 0
        IncYr = IncYi
        # Intercambiamos dx y dy si dY es mayor
        dX, dY = dY, dX  
        
    # determinar cuándo avanzar en una dirección recta
    avR = 2 * dY
    
    #cuán lejos estamos de la línea ideal en cada paso
    av = avR - dX
    
    #se utiliza cuando hacemos un avance inclinado
    avI = av - dX

    # Valores iniciales
    x = x1
    y = y1

    glBegin(GL_POINTS)
    
    while x != x2 or y != y2:
        #Se dibuja
        glVertex2f(x, y)
        
        #Si la distancia de la línea ideal es mayor o igual a cero
        if av >= 0:
            x += IncXi  # Incremento en x inclinado
            y += IncYi  # Incremento en y inclinado
            av += avI   # Actualizamos error
            
        #Si la distancia de la línea ideal es menor a cer0
        else:
            x += IncXr  # Incremento en x recto
            y += IncYr  # Incremento en y recto
            av += avR   # Actualizamos error
    
    # Dibujamos el último punto
    glVertex2f(x2, y2)  
    glEnd()
    
def plot_function(x1, x2, y1, y2):
    glColor3f(0.0, 0.0, 1.0)
    LineaBresenham(-200, -100, 200, 100) 
    LineaBresenham(-300, 150, 300, -150)

def init():
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: ejes 2D")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-450, 450, -300, 300)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0, 0, 0, 0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glShadeModel(GL_FLAT)

init()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT)
    Axis()
    plot_function()  
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()