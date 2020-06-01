#importa bibliotecas necessarias
import pygame
import random
from configuracao import largura_background, altura_background, largura_heroi, altura_heroi, largura_tiro, altura_tiro, largura_boss, altura_boss, largura_poderzin, altura_poderzin, FPS, SPEEDX
from assets import load_assets
from sprites import Personagem, Boss, Poderzin, Bullet

def screen_game(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    #Grupos
    all_sprites = pygame.sprite.Group()
    all_poderzin = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_poderzin'] = all_poderzin
    groups['all_bullets'] = all_bullets

    #Criando o Chefão
    chefão = Boss(groups, assets)
    all_sprites.add(chefão)
    #Criando o jogador
    player = Personagem(groups, assets)
    all_sprites.add(player)
    #Criando os poderes do boss
    for i in range(8):
        poder = Poderzin(assets, chefão)
        all_sprites.add(poder)
        all_poderzin.add(poder) 

    # Possíveis estados do jogador
    STILL = 0
    JUMPING = 1
    FALLING = 2

    PLAYING = 0
    DONE = 1
    state = PLAYING

    # ======== Loop principal =========

    while state != DONE:
        clock.tick(FPS) 

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = DONE

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEEDX
                if event.key == pygame.K_RIGHT:
                    player.speedx += SPEEDX
                if event.key == pygame.K_UP:
                    player.pulo()
                if event.key == pygame.K_SPACE:
                    player.shoot()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEEDX
                if event.key == pygame.K_RIGHT:
                    player.speedx -= SPEEDX
            
        #atualiza estado do jogo
        all_sprites.update()

        #gera sáidas
        window.fill((46, 139, 87))
        window.blit(assets['background'],(0,0))
        
        #desenhando sprites
        all_sprites.draw(window)

        #mostra o novo frame para o jogador
        pygame.display.update()

