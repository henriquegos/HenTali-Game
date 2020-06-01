import pygame

# Variáveis 

#Dimensões da Tela
largura_janela = 1080
altura_janela = 540

#Dimensões do fundo
largura_background = 1080
altura_background = 540

#Dimensões do herói
largura_heroi = 80
altura_heroi = 80

#Dimensões do tiro
largura_tiro = 160
altura_tiro = 80

#Dimensões do chefe
largura_boss = 160
altura_boss = 160

#Dimensões do poder
largura_poderzin = 40
altura_poderzin = 40

gravidade = 2
tamanho_pulo = 30
altura_chão = altura_janela - 45
velo_tiro = 5
SPEEDX = 3
FPS = 60
TITULO = 'Mariozinho'

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Possíveis estados do jogador
STILL = 0
JUMPING = 1
FALLING = 2

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
