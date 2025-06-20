import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

from objeto import Objeto3D
from camera import configurar_camera
from iluminacao import configurar_iluminacao
from piso import desenhar_piso


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)

    glClearColor(0.529, 0.808, 0.922, 1)  # Fundo azul céu

    configurar_iluminacao()
    objeto = Objeto3D()

    rodar = True

    # Visão inicial
    angulo_x, angulo_y = 20, 180  # Câmera inclinada
    zoom = -15

    # Estado do carro
    posicao_x, posicao_z = 0, 0
    angulo_carro = 0  # Rotação do carro no eixo Y

    while rodar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodar = False

        teclas = pygame.key.get_pressed()

        # Controle da câmera (rotação em volta do centro)
        if teclas[pygame.K_LEFT]:
            angulo_y += 2
        if teclas[pygame.K_RIGHT]:
            angulo_y -= 2
        if teclas[pygame.K_UP]:
            angulo_x += 2
        if teclas[pygame.K_DOWN]:
            angulo_x -= 2

        # Limitar o angulo vertical da câmera
        angulo_x = max(-89, min(89, angulo_x))

        # Controle do carro
        # Girar no próprio eixo
        if teclas[pygame.K_a]:
            angulo_carro += 3  # Vira para a esquerda
        if teclas[pygame.K_d]:
            angulo_carro -= 3  # Vira para a direita

        # Movimentação para frente e trás baseado na rotação
        direcao_x = math.sin(math.radians(angulo_carro))
        direcao_z = math.cos(math.radians(angulo_carro))

        if teclas[pygame.K_w]:
            novo_x = posicao_x + 0.1 * direcao_x
            novo_z = posicao_z + 0.1 * direcao_z
            if -9.8 <= novo_x <= 9.8 and -9.8 <= novo_z <= 9.8:
                posicao_x = novo_x
                posicao_z = novo_z

        if teclas[pygame.K_s]:
            novo_x = posicao_x - 0.1 * direcao_x
            novo_z = posicao_z - 0.1 * direcao_z
            if -9.8 <= novo_x <= 9.8 and -9.8 <= novo_z <= 9.8:
                posicao_x = novo_x
                posicao_z = novo_z

        # Zoom da câmera (U e J)
        if teclas[pygame.K_u]:
            zoom += 0.2  # Aproxima
        if teclas[pygame.K_j]:
            zoom -= 0.2  # Afasta
        zoom = max(-25, min(-5, zoom))  # Limita o zoom

        # Renderização
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        configurar_camera(zoom, angulo_x, angulo_y)

        desenhar_piso()

        glPushMatrix()
        glTranslatef(posicao_x, 0.2, posicao_z)  # Move o carro para sua posição
        glRotatef(angulo_carro, 0, 1, 0)  # Rotaciona o carro no próprio eixo Y
        objeto.desenhar()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
