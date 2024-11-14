import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np

class OpMat:
    
    def __init__(self):
        # M tranformacion
        self.T = np.identity(4)  # Translacion
        self.R = np.identity(4)  # Rotacion 
        self.E = np.identity(4)  # Escalado
        self.A = np.identity(4) 
        self.M = np.identity(4)  # Modelado
        self.stack = []
        
    def loadId(self):
        self.T = np.identity(4)
        self.R = np.identity(4)
        self.E = np.identity(4)
        self.A = np.identity(4)
        self.M = np.identity(4)

    def translate(self, tx, ty, tz):
        self.T = np.identity(4)
        self.T[0][3] = tx
        self.T[1][3] = ty
        self.T[2][3] = tz
        self.M = np.dot(self.T, self.M)
    
    def scale(self, sx, sy, sz):
        self.E = np.identity(4)
        self.E[0][0] = sx
        self.E[1][1] = sy
        self.E[2][2] = sz
        self.M = np.dot(self.E, self.M)
    
    def rotateZ(self, deg):
        rad = math.radians(deg)
        cos_theta = math.cos(rad)
        sin_theta = math.sin(rad)
        
        self.R = np.identity(4)
        
        self.R[0][0] = cos_theta
        self.R[0][1] = -sin_theta
        self.R[1][0] = sin_theta
        self.R[1][1] = cos_theta
        
        self.M = np.dot(self.R, self.M)
    
    def rotateX(self, deg):
        rad = math.radians(deg)
        cos_theta = math.cos(rad)
        sin_theta = math.sin(rad)
        
        self.R = np.identity(4)
        
        self.R[1][1] = cos_theta
        self.R[1][2] = -sin_theta
        self.R[2][1] = sin_theta
        self.R[2][2] = cos_theta
        
        self.M = np.dot(self.R, self.M)
    
    def rotateY(self, deg):
        rad = math.radians(deg)
        cos_theta = math.cos(rad)
        sin_theta = math.sin(rad)
        
        self.R = np.identity(4)
        
        self.R[0][0] = cos_theta
        self.R[0][2] = sin_theta
        self.R[2][0] = -sin_theta
        self.R[2][2] = cos_theta
        
        self.M = np.dot(self.R, self.M)
        
    def rotate(self, theta, x, y, z): 
        # si el eje es el correcto
        if x == 1.0 and y == 0.0 and z == 0.0:
            self.rotateX(theta)
        elif x == 0.0 and y == 1.0 and z == 0.0:
            self.rotateY(theta)
        elif x == 0.0 and y == 0.0 and z == 1.0:
            self.rotateZ(theta)
        else:
            magnitud = math.sqrt( ((x**2) + (y**2) + (z**2)) )

            a = x/magnitud
            b = y/magnitud
            c = z/magnitud
            d = math.sqrt(((b**2)+(c**2)))
            cos_theta = math.cos(math.radians(theta))
            sin_theta = math.sin(math.radians(theta))
            a_2 = a*a
            b_2 = b*b
            c_2 = c*c
            d_2 = d*d
            self.R = np.array([
                [d_2*cos_theta+a_2, b*a*(-cos_theta+1)-c*sin_theta, b*sin_theta+c*a*(-cos_theta+1), 0],
                [c*sin_theta-b*a*cos_theta+b*a, (c_2*cos_theta+b_2*a_2*cos_theta+d_2*b_2)/d_2, (c*(d_2*b-a*(c*sin_theta-b*a*cos_theta))-b*(c*cos_theta+b*a*sin_theta))/d_2, 0],
                [-b*sin_theta-c*a*cos_theta+c*a, (c*(c*a*sin_theta-b*cos_theta)+b*(c*d_2-a*(-b*sin_theta-c*a*cos_theta)))/d_2, (b_2*cos_theta+c_2*a_2*cos_theta+c_2*d_2)/d_2, 0],
                [0,0,0,1]
            ])
            self.M @= self.R
    
    def mult_Points(self, points):
        for i in range(len(points)):
            points[i] = np.dot(self.M, points[i])

    def push(self):
        self.stack.append(self.M.copy())
    
    def pop(self):
        if len(self.stack) > 0:
            self.M = self.stack.pop()
        else:
            print("Stack is empty")
