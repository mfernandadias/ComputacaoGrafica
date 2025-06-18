import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from carro import Carro
from camera import Camera
from iluminacao import Iluminacao

def main():
    pygame.init()
    glutInit()

    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Carro 3D Interativo")

    glEnable(GL_DEPTH_TEST)

    carro = Carro()
    camera = Camera()
    luz = Iluminacao()
    luz.configurar()

    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                return
            if evento.type == KEYDOWN:
                if evento.key == K_w:
                    carro.mover_frente()
                if evento.key == K_a:
                    carro.girar(5)
                if evento.key == K_d:
                    carro.girar(-5)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        camera.atualizar(carro.posicao)
        carro.desenhar()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

# done = False
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     pygame.display.flip()
#     pygame.time.wait(100)
# pygame.quit()

