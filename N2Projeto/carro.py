from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math

class Carro:
    def __init__(self):
        self.posicao = np.array([0.0, 0.0, 0.0])
        self.rotacao = 0.0
        self.escala = 1.0

    def desenhar(self):
        glPushMatrix()
        glTranslatef(*self.posicao)
        glRotatef(self.rotacao, 0, 1, 0)
        glScalef(self.escala, self.escala, self.escala)

        # Corpo do carro
        glColor3f(1.0, 0.0, 0.0)
        glutSolidCube(1)

        glPopMatrix()

    def mover_frente(self):
        ang_rad = math.radians(self.rotacao)
        self.posicao[0] += math.sin(ang_rad) * 0.1
        self.posicao[2] += math.cos(ang_rad) * 0.1

    def girar(self, angulo):
        self.rotacao += angulo
