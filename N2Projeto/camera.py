from OpenGL.GL import *
from OpenGL.GLU import *

import math

class Camera:
    def __init__(self):
        self.distancia = 5.0
        self.pitch = 20
        self.yaw = 0

    def atualizar(self, alvo):
        pitch_rad = math.radians(self.pitch)
        yaw_rad = math.radians(self.yaw)
        camX = alvo[0] + self.distancia * math.cos(pitch_rad) * math.sin(yaw_rad)
        camY = alvo[1] + self.distancia * math.sin(pitch_rad)
        camZ = alvo[2] + self.distancia * math.cos(pitch_rad) * math.cos(yaw_rad)

        glLoadIdentity()
        gluLookAt(camX, camY, camZ, alvo[0], alvo[1], alvo[2], 0, 1, 0)
