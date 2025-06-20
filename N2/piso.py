from OpenGL.GL import *

def desenhar_piso():
    glDisable(GL_LIGHTING)  # Desativa a iluminação para aplicar cor sólida

    glColor3f(0.133, 0.545, 0.133)  # Verde floresta (forest green)

    glBegin(GL_QUADS)
    glVertex3f(-10, -0.5, -10)
    glVertex3f(10, -0.5, -10)
    glVertex3f(10, -0.5, 10)
    glVertex3f(-10, -0.5, 10)
    glEnd()

    glEnable(GL_LIGHTING)  # Reativa a iluminação para o carro