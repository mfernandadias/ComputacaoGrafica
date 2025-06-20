from OpenGL.GL import *
from OpenGL.GLU import *


class Objeto3D:
    def __init__(self):
        # Base do carro
        self.vertices_base = (
            (-1, -0.25, -2), (1, -0.25, -2), (1, 0.25, -2), (-1, 0.25, -2),
            (-1, -0.25, 2), (1, -0.25, 2), (1, 0.25, 2), (-1, 0.25, 2),
        )

        # Teto do carro
        self.vertices_teto = (
            (-0.6, 0.25, -1.2), (0.6, 0.25, -1.2), (0.6, 0.85, -1.2), (-0.6, 0.85, -1.2),
            (-0.6, 0.25, 1.2), (0.6, 0.25, 1.2), (0.6, 0.85, 1.2), (-0.6, 0.85, 1.2),
        )

        # Faces da base e do teto
        self.faces = (
            # Base
            (0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4),
            (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5),
            # Teto
            (8, 9, 10, 11), (12, 13, 14, 15), (8, 9, 13, 12),
            (10, 11, 15, 14), (8, 11, 15, 12), (9, 10, 14, 13),
        )

        # Rodas
        self.rodas = [
            (-0.7, -0.5, -1.5), (0.7, -0.5, -1.5),
            (-0.7, -0.5, 1.5), (0.7, -0.5, 1.5),
        ]

        # Janelas (deslocadas suavemente)
        self.janelas = (
            # Lateral esquerda
            ((-0.625, 0.3, -1.1), (-0.625, 0.8, -1.1), (-0.625, 0.8, 1.1), (-0.625, 0.3, 1.1)),
            # Lateral direita
            ((0.625, 0.3, -1.1), (0.625, 0.8, -1.1), (0.625, 0.8, 1.1), (0.625, 0.3, 1.1)),
            # Frente
            ((-0.5, 0.3, 1.225), (0.5, 0.3, 1.225), (0.5, 0.8, 1.225), (-0.5, 0.8, 1.225)),
            # Trás
            ((-0.5, 0.3, -1.225), (0.5, 0.3, -1.225), (0.5, 0.8, -1.225), (-0.5, 0.8, -1.225)),
        )

        # Faróis
        self.farois = [
            (-0.7, 0.05, 2.05),
            (0.7, 0.05, 2.05),
        ]

        # Lanternas
        self.lanternas = [
            (-0.7, 0.05, -2.05),
            (0.7, 0.05, -2.05),
        ]

    def desenhar(self):
        # Corpo
        glColor3f(1, 0, 0)
        glBegin(GL_QUADS)
        for face in self.faces:
            for vertice in face:
                if vertice < 8:
                    glVertex3fv(self.vertices_base[vertice])
                else:
                    glVertex3fv(self.vertices_teto[vertice - 8])
        glEnd()

        # Janelas (saltadas suavemente)
        glDisable(GL_LIGHTING)
        glColor3f(0.2, 0.2, 0.8)
        glBegin(GL_QUADS)
        for janela in self.janelas:
            for vertice in janela:
                glVertex3fv(vertice)
        glEnd()

        # Faróis
        glColor3f(1, 1, 0.8)
        glBegin(GL_QUADS)
        for farol in self.farois:
            x, y, z = farol
            tamanho = 0.1
            glVertex3f(x - tamanho, y - tamanho, z)
            glVertex3f(x + tamanho, y - tamanho, z)
            glVertex3f(x + tamanho, y + tamanho, z)
            glVertex3f(x - tamanho, y + tamanho, z)
        glEnd()

        # Lanternas traseiras
        glColor3f(1, 0, 0)
        glBegin(GL_QUADS)
        for lanterna in self.lanternas:
            x, y, z = lanterna
            tamanho = 0.1
            glVertex3f(x - tamanho, y - tamanho, z)
            glVertex3f(x + tamanho, y - tamanho, z)
            glVertex3f(x + tamanho, y + tamanho, z)
            glVertex3f(x - tamanho, y + tamanho, z)
        glEnd()

        glEnable(GL_LIGHTING)

        # Rodas
        for roda in self.rodas:
            self.desenhar_roda(roda[0], roda[1], roda[2])

    def desenhar_roda(self, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(90, 0, 1, 0)
        quadric = gluNewQuadric()
        gluDisk(quadric, 0, 0.2, 20, 1)
        gluCylinder(quadric, 0.2, 0.2, 0.2, 20, 1)
        glTranslatef(0, 0, 0.2)
        gluDisk(quadric, 0, 0.2, 20, 1)
        glPopMatrix()
