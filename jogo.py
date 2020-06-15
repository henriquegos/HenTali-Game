#importa bibliotecas necessarias
import pygame
import random
from configuracao import largura_background, altura_background, largura_heroi, altura_heroi, largura_tiro, altura_tiro, largura_boss, altura_boss, largura_poderzin, altura_poderzin, FPS, SPEEDX, QUIT, LOSE, WON
from assets import load_assets, SOUND_GOAL, SOUND_LOSES, SOUND_JUMP, SOUND_HIT_HERO, SOUND_HIT_BOSS, SOUND_GAMING
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

    som_game = assets[SOUND_GAMING]
    som_game.play()
    som_game.set_volume(0.02)

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


    keys_down = {}
    lives_hero = 3
    lives_boss = 5

    # ======== Loop principal =========
    running = True
    while running:
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
                    som_pulo = assets[SOUND_JUMP]
                    som_pulo.set_volume(0.2)
                    som_pulo.play()
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
        #Colisões entre poder do boss e personagem
        hits = pygame.sprite.spritecollide(player, all_poderzin, True, pygame.sprite.collide_mask)
        if len(hits) > 0:
            som_hit_hero = assets[SOUND_HIT_HERO]
            som_hit_hero.set_volume(0.05)
            som_hit_hero.play()
            lives_hero -= 1
        if lives_hero == 0:
            som_game.set_volume(0)
            som_loses = pygame.mixer.Sound('assets/snd/death.ogg')
            som_loses.set_volume(0.03)
            som_loses.play()
            time.sleep(2.8)
            state = LOSE
            running = False 
        #Colisões entre poder do personagem e boss
        hits_2 = pygame.sprite.spritecollide(chefão, all_bullets, True, pygame.sprite.collide_mask)
        if len(hits_2) > 0:
            som_hit_boss = assets[SOUND_HIT_BOSS]
            som_hit_boss.set_volume(0.05)
            som_hit_boss.play()
            lives_boss -= 1
        if lives_boss == 0:
            som_game.set_volume(0)
            som_goal = assets[SOUND_GOAL]
            som_goal.set_volume(0.6)
            som_goal.play()
            time.sleep(7.8)
            state = WON
            running = False

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
