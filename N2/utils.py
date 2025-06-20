import pygame
from OpenGL.GL import *

def carregar_textura(caminho):
    textura_surface = pygame.image.load(caminho)
    textura_dados = pygame.image.tostring(textura_surface, "RGBA", 1)
    largura, altura = textura_surface.get_size()

    textura_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, largura, altura, 0, GL_RGBA, GL_UNSIGNED_BYTE, textura_dados)

    glEnable(GL_TEXTURE_2D)

    return textura_id