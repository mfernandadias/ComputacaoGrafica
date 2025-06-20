from OpenGL.GL import *

def aplicar_transformacoes(angulo_x, angulo_y, pos_x, pos_z, escala):
    glLoadIdentity()
    glTranslatef(pos_x, 0.0, pos_z)
    glScalef(escala, escala, escala)
    glRotatef(angulo_x, 1, 0, 0)
    glRotatef(angulo_y, 0, 1, 0)