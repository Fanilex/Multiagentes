import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np

class Piramide:
    
    def __init__(self, op):
        
        # coordenadas de los vértices de la pirámide
        self.points = np.array([
            [1.0, 0.0, 1.0, 1.0],
            [1.0, 0.0, -1.0, 1.0],
            [-1.0, 0.0, -1.0, 1.0],
            [-1.0, 0.0, 1.0, 1.0],
            [0.0, 3.0, 0.0, 1.0]
        ])
        
        self.op3D = op
        self.position = np.array([0.0, 0.0, 0.0])
        self.delta = np.array([0.0, 0.0, 0.0])
        self.theta = 0.0
        self.delta_theta = 1.0
        self.rotAxis = np.array([1.0, 1.0, 1.0])
        self.scale = 1.0
        self.delta_scale = 0.01
        self.newdeg = lambda deg, delta_deg: deg + delta_deg if deg + delta_deg < 360.0 else (deg + delta_deg) % 360.0
        self.angle = 0.0
        self.delta_angle = 2.0  # Velocidad
        self.a = 5.0  # Escala del infinito

    def setPosition(self, x, y, z):
        self.position = np.array([x, y, z])

    def setDelta(self, dx, dy, dz):
        self.delta = np.array([dx, dy, dz])

    def setTheta(self, theta):
        self.theta = theta

    def setDeltaTheta(self, delta_theta):
        self.delta_theta = delta_theta

    def setRotAxis(self, x, y, z):
        self.rotAxis = np.array([x, y, z])

    def setScale(self, scale):
        self.scale = scale

    def setDeltaScale(self, delta_scale):
        self.delta_scale = delta_scale

    def update(self):
        # Paramétricos
        # Actualizar el ángulo 
        self.angle += self.delta_angle
        if self.angle >= 360.0:
            self.angle -= 360.0

        # Ecuaciones para el inifnito
        t = math.radians(self.angle)
        a = self.a  

        denom = math.sin(t)**2 + 1
        if denom == 0:
            denom = 0.0001  # EVitar el 0

        # Coordenadas X y Z
        self.position[0] = (a * math.sqrt(2) * math.cos(t)) / denom
        self.position[1] = 0.0  
        self.position[2] = (a * math.sqrt(2) * math.cos(t) * math.sin(t)) / denom

        # Actualizar theta para la rotación
        self.theta = self.newdeg(self.theta, self.delta_theta)

    def draw(self):
        glBegin(GL_QUADS)
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glEnd()
        
        glBegin(GL_LINES)
        glVertex3f(self.points[0][0], self.points[0][1], self.points[0][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(self.points[1][0], self.points[1][1], self.points[1][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(self.points[2][0], self.points[2][1], self.points[2][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(self.points[3][0], self.points[3][1], self.points[3][2])
        glVertex3f(self.points[4][0], self.points[4][1], self.points[4][2])
        glEnd()
    
    def render(self):
        self.op3D.push()
        self.op3D.translate(self.position[0], self.position[1], self.position[2])
        self.op3D.rotate(self.theta, self.rotAxis[0], self.rotAxis[1], self.rotAxis[2])
        self.op3D.scale(self.scale, self.scale, self.scale)
        pointsR = self.points.copy()
        self.op3D.mult_Points(pointsR)
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex3f(pointsR[0][0], pointsR[0][1], pointsR[0][2])
        glVertex3f(pointsR[1][0], pointsR[1][1], pointsR[1][2])
        glVertex3f(pointsR[2][0], pointsR[2][1], pointsR[2][2])
        glVertex3f(pointsR[3][0], pointsR[3][1], pointsR[3][2])        
        glEnd()
        
        glBegin(GL_LINES)
        glVertex3f(pointsR[0][0], pointsR[0][1], pointsR[0][2])
        glVertex3f(pointsR[4][0], pointsR[4][1], pointsR[4][2])
        glEnd()
        
        glBegin(GL_LINES)
        glVertex3f(pointsR[1][0], pointsR[1][1], pointsR[1][2])
        glVertex3f(pointsR[4][0], pointsR[4][1], pointsR[4][2])
        glEnd()
        
        glBegin(GL_LINES)
        glVertex3f(pointsR[2][0], pointsR[2][1], pointsR[2][2])
        glVertex3f(pointsR[4][0], pointsR[4][1], pointsR[4][2])
        glEnd()
        
        glBegin(GL_LINES)
        glVertex3f(pointsR[3][0], pointsR[3][1], pointsR[3][2])
        glVertex3f(pointsR[4][0], pointsR[4][1], pointsR[4][2])
        glEnd()
        self.op3D.pop()
