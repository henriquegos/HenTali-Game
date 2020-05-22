import pygame

pygame.init()

# Variáveis
largura_janela = 1080
altura_janela = 540

window = pygame.display.set_mode((largura_janela,altura_janela))
pygame.display.set_caption('Mariozinho')

mario_img = pygame.image.load('assets/img/nego_mario.png').convert_alpha()
mario_img = pygame.transform.scale(mario_img,(128,128))

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((46, 139, 87))
    window.blit(mario_img,(32,430))

    pygame.display.update()

pygame.quit()