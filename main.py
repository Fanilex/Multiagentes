import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class OpMat:
    def __init__(self):
        self.M = np.identity(3)
        self.stack = []

    def translate(self, tx, ty):
        #mis varaibles de cambio tx y ty
        T = np.array([[1, 0, 0], [0, 1, 0], [tx, ty, 1]])
        self.M = self.M @ T

    def scale(self, sx, sy):
        S = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
        self.M = self.M @ S
        
        #delta de los angulos
    def rotate(self, angle):
        rad = np.radians(angle)
        cos_theta = np.cos(rad)
        sin_theta = np.sin(rad)
        R = np.array([[cos_theta, -sin_theta, 0], [sin_theta, cos_theta, 0], [0, 0, 1]])
        self.M = self.M @ R
        
    def loadIU(self):
        self.M = np.identity(3)

    def push(self):
        self.stack.append(self.M.copy())

    def pop(self):
        self.M = self.stack.pop()

    def mult_points(self, points):
        transformed_points = []
        for x, y in points:
            vec = np.array([x, y, 1])
            # Matrix por el vertice
            transformed_vec = vec @ self.M
            # Vértice ya trasnformado
            transformed_points.append((transformed_vec[0], transformed_vec[1]))
        return transformed_points

class Triangulo:
    def __init__(self, vertices):
        self.vertices = vertices

    def Draw(self, opmat):
        transformed_vertices = self.vertices.copy()
        transformed_vertices = opmat.mult_points(transformed_vertices)
        for i in range(3):
            x1, y1 = transformed_vertices[i]
            x2, y2 = transformed_vertices[(i + 1) % 3]
            LineaBresenham(int(x1), int(x2), int(y1), int(y2))

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
    screen = pygame.display.set_mode((900, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Triangulos") 

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-450, 450, -300, 300)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(255, 255, 255, 0) 
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  
    glShadeModel(GL_FLAT)

    opmat1 = OpMat()

    triangle1 = Triangulo([(-30, -30), (30, -30), (0, 60)])  
    
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

        # Triangulo 1
        opmat1.push()
        opmat1.rotate(angle1) 
        glColor3f(1.0, 0.0, 0.0)  
        triangle1.Draw(opmat1)
        opmat1.pop()

        # Triangulo 2
        opmat1.push()
        opmat1.translate(150, 0) 
        opmat1.rotate(angle2) 
        opmat1.scale(0.5,0.5)
        glColor3f(0.0, 1.0, 0.0)
        opmat1.push()
        triangle1.Draw(opmat1)
        opmat1.pop()
        opmat1.pop()

        # 3
        opmat1.push()
        opmat1.translate(150, -15) 
        opmat1.rotate(angle3) 
        opmat1.scale(0.7,0.7)
        glColor3f(0.0, 0.0, 1.0) 
        triangle1.Draw(opmat1) 
        opmat1.pop()

        angle1 += 1
        angle2 += 2
        angle3 += 3

        pygame.display.flip() 
        pygame.time.wait(30)

    pygame.quit()

if __name__ == "__main__":
    main()
