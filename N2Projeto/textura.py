from OpenGL.GL import *
import cv2

class Textura:
    def __init__(self, caminho):
        self.id = self.carregar_textura(caminho)

    def carregar_textura(self, caminho):
        imagem = cv2.imread(caminho)
        imagem = cv2.flip(imagem, 0)
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

        textura = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textura)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imagem.shape[1], imagem.shape[0], 0, GL_RGB, GL_UNSIGNED_BYTE, imagem)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        return textura
