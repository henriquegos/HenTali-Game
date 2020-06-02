import pygame 
from configuracao import FPS, BLACK, GAME, QUIT
def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    first_background = pygame.image.load('assets/img/start_screen.png').convert()
    first_background_rect = first_background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(first_background, first_background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state