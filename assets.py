import pygame
from configuracao import largura_background, altura_background, largura_heroi, altura_heroi, largura_tiro, altura_tiro, largura_boss, altura_boss, largura_poderzin, altura_poderzin

BACKGROUND = 'background'
MARIO_IMG = 'mario_img'
BULLET_IMG = 'bullet_img'
BOSS_IMG = 'boss_img'
PODER_IMG = 'poder_img'


#assets
def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load('assets/img/mario_backgroud.png').convert_alpha()
    assets[BACKGROUND] = pygame.transform.scale(assets['background'],(largura_background,altura_background))
    assets[MARIO_IMG] = pygame.image.load('assets/img/nego_mario.png').convert_alpha()
    assets[MARIO_IMG] = pygame.transform.scale(assets['mario_img'],(largura_heroi,altura_heroi))
    assets[BULLET_IMG] = pygame.image.load('assets/img/mario_especial.png').convert_alpha()
    assets[BULLET_IMG] = pygame.transform.scale(assets['bullet_img'],(largura_tiro,altura_tiro))
    assets[BOSS_IMG] = pygame.image.load('assets/img/boss_mario.png').convert_alpha()
    assets[BOSS_IMG] = pygame.transform.scale(assets['boss_img'],(largura_boss, altura_boss))
    assets[PODER_IMG] = pygame.image.load('assets/img/poder_boss.png').convert_alpha()
    assets[PODER_IMG] = pygame.transform.scale(assets['poder_img'], (largura_poderzin, altura_poderzin))
    return assets  
