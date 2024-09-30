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

def plot_function():
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    
    num_points = 720
    theta = np.linspace(0, 2 * np.pi, num_points)
    r = -3 + 4 * np.sin(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    for i in range(num_points):
        glVertex2f(x[i] * 20, y[i] * 20)  
    
    glEnd()

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