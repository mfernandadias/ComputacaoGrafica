from OpenGL.GL import *
from OpenGL.GLU import *


def configurar_camera(zoom, angulo_x, angulo_y):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)

    glTranslatef(0.0, 0.0, zoom)
    glRotatef(angulo_x, 1, 0, 0)
    glRotatef(angulo_y, 0, 1, 0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()