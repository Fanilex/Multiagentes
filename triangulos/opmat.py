import numpy as np

class OpMat:
    def __init__(self):
        self.M = np.identity(3)
        self.stack = []

    def translate(self, tx, ty):
        #mis varaibles de cambio tx y ty
        T = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
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
            transformed_vec = (self.M @ vec.T).T
            transformed_points.append((transformed_vec[0], transformed_vec[1]))
        return transformed_points