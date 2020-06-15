import pygame 
from configuracao import largura_background, altura_background, FPS, BLACK, GAME, QUIT

pygame.mixer.init()

som_inicial = pygame.mixer.Sound('assets/snd/maintheme.ogg')
som_inicial.set_volume(0.03)

def fade(width, height, screen): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)

def won_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela ganhou
    first_background = pygame.image.load('assets/img/tela_youwon.png').convert()
    first_background_rect = first_background.get_rect() 
    fade_estado = False 
    som_inicial.play()

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
            if event.type == pygame.KEYUP: #Outra opção pra sair do jogo, apertar a tecla Q
                if event.key == pygame.K_q:
                    state = QUIT
                    running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: #Caso o jogador queira iniciar o jogo, precisa apertar "espaço"
                    fade(largura_background, altura_background, screen)
                    fade_estado = True
                    som_inicial.set_volume(0)
                    state = GAME
                    running = False 
                    
        if not fade_estado:
            # A cada loop, redesenha o fundo e os sprites
            screen.fill(BLACK)
            screen.blit(first_background, first_background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state 