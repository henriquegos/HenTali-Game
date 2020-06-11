#importa bibliotecas necessarias
import pygame
import random
from configuracao import largura_background, altura_background, largura_heroi, altura_heroi, largura_tiro, altura_tiro, largura_boss, altura_boss, largura_poderzin, altura_poderzin, FPS, SPEEDX
from assets import load_assets, SOUND_GOAL, SOUND_LOSES
from sprites import Personagem, Boss, Poderzin, Bullet
import time

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
    QUIT = 1
    state = PLAYING

    keys_down = {}
    lives_hero = 3
    lives_boss = 12

    # ======== Loop principal =========

    while state != QUIT:
        clock.tick(FPS) 

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = QUIT
                pygame.quit() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEEDX
                if event.key == pygame.K_RIGHT:
                    player.speedx += SPEEDX
                if event.key == pygame.K_UP:
                    player.pulo()
                if event.key == pygame.K_SPACE:
                    player.shoot()
                if event.key == pygame.K_q:
                    state = QUIT
                    pygame.quit()
           
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEEDX
                if event.key == pygame.K_RIGHT:
                    player.speedx -= SPEEDX

        hits = pygame.sprite.spritecollide(player, all_poderzin, True, pygame.sprite.collide_mask)
        if len(hits) > 0:
            lives_hero -= 1
            if lives_hero == 0:
                som_loses = assets[SOUND_LOSES]
                som_loses.set_volume(0.7)
                som_loses.play()
                time.sleep(3)
                state = QUIT
                pygame.quit() 

        hits = pygame.sprite.spritecollide(chefão, all_bullets, True, pygame.sprite.collide_mask)
        if len(hits) > 0:
            lives_boss -= 1
            if lives_boss == 0:
                som_goal = assets[SOUND_GOAL]
                som_goal.set_volume(0.7)
                som_goal.play()
                time.sleep(8)
                state = QUIT
                pygame.quit()

        #atualiza estado do jogo
        all_sprites.update()

        #gera sáidas
        window.fill((46, 139, 87))
        window.blit(assets['background'],(0,0))

        # Desenhando as vidas do player
        text_surface = assets["score_font"].render(chr(9829) * lives_hero, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, altura_background - 10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas do chefão
        text_surface = assets["score_font"].render(chr(9829) * lives_boss, True, (104, 34, 139))
        text_rect = text_surface.get_rect()
        text_rect.topright = (largura_background - 10, 10)
        window.blit(text_surface, text_rect)
        
        #desenhando sprites
        all_sprites.draw(window)

        #mostra o novo frame para o jogador
        pygame.display.update()
    
    return state