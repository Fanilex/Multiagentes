from OpenGL.GL import *
from opmat import OpMat

class Triangulo:
    def __init__(self, opmat):
        self.vertices = [(-1, -1), (1, -1), (0, 2)]
    
    def update(self, opmat, tx=0, ty=0, angle=0, scale_x=1, scale_y=1):
        opmat.push()
        opmat.translate(tx, ty)
        opmat.rotate(angle)
        opmat.scale(scale_x, scale_y)
        self.transformed_vertices = opmat.mult_points(self.vertices)
        opmat.pop()

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
