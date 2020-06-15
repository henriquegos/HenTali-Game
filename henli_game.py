import pygame
import random 
from configuracao import largura_janela, altura_janela, GAME, QUIT, INIT, TITULO, WON, LOSE
from tela_inicio import init_screen 
from tela_perdeu import lose_screen
from tela_ganhou import won_screen
from jogo import screen_game

#inicia frameworks
pygame.init()
pygame.mixer.init()

#Janela
window = pygame.display.set_mode((largura_janela,altura_janela))
pygame.display.set_caption(TITULO)


state = INIT 
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = screen_game(window)
    elif state == LOSE:
        state = lose_screen(window)
    elif state == WON:
        state = won_screen(window)
    else:
        state = QUIT

pygame.quit()
