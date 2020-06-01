import pygame
import random 
from configuracao import largura_janela, altura_janela, GAME, QUIT, INIT, TITULO
from tela_inicio import init_screen 
from jogo import screen_game

#pygame.init()inicia framework
pygame.init()

#Janela
window = pygame.display.set_mode((largura_janela,altura_janela))
pygame.display.set_caption(TITULO)

state = INIT 
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = screen_game(window)
    else:
        state = QUIT

pygame.quit()
