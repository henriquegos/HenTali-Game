import pygame
import random
from configuracao import largura_janela, altura_janela, largura_background, altura_background, largura_heroi, altura_heroi, largura_tiro, altura_tiro, largura_boss, altura_boss, largura_poderzin, altura_poderzin, gravidade, tamanho_pulo, altura_chão, velo_tiro, SPEEDX, FPS, STILL, JUMPING, FALLING
from assets import BACKGROUND, MARIO_IMG, BULLET_IMG, BOSS_IMG, PODER_IMG, SOUND_GAMING      

#Classe Personagem que representa o herói
class Personagem(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[MARIO_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 80 
        self.rect.bottom = altura_chão
        self.groups = groups
        self.assets = assets
        som_game = self.assets[SOUND_GAMING]
        som_game.play()
        som_game.set_volume(0.02)
        self.speedx = 0
        self.speedy = 0
        self.state = STILL

        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500
    
    # Atualiza posição do herói
    def update(self):
        self.rect.x += self.speedx
        self.speedy += gravidade
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        if self.rect.bottom > altura_chão:
            self.rect.bottom = altura_chão
            self.speedy = 0 
            self.state = STILL

        if self.rect.right > largura_janela:
            self.rect.right = largura_janela
        if self.rect.left < 0:
            self.rect.left = 0
    
    # Responsável pelo pulo do personagem
    def pulo(self):
        if self.state == STILL:
            self.speedy -= tamanho_pulo
            self.state = JUMPING
    
    # Responsável pelo poderzinho do personagem
    def shoot(self):

        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_shot

        #verifica se pode atualizar posição do poderzinho do herói
        if elapsed_ticks > self.shoot_ticks:
            self.last_shot = now
            new_bullet = Bullet(self.assets, self.rect.centery, self.rect.left)
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_bullets'].add(new_bullet)
    
#Classe Boss que representa o chefão
class Boss(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BOSS_IMG]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(largura_janela/2, largura_janela - largura_boss)
        self.rect.bottom = random.randint(altura_boss, altura_chão)
        self.groups = groups
        self.assets = assets

        self.last_poder = pygame.time.get_ticks()
        self.pooder_ticks = 5000

        self.last_posicao = pygame.time.get_ticks()
        self.poosicao_ticks = 5000
    
    # Responsável por atualizar a posição do boss
    def update(self):        
        ahora = pygame.time.get_ticks()
        transcurrido_ticks = ahora - self.last_posicao

        #verifica se pode atualizar posição do boss
        if transcurrido_ticks > self.poosicao_ticks:
            self.last_posicao = ahora
            #atualizando posição do boss
            self.rect.centerx = random.randint(largura_janela/2, largura_janela - largura_boss)
            self.rect.bottom = random.randint(altura_boss, altura_chão)

    # Responsável pelo poderzinho do Chefão
    def poder(self):
        agora = pygame.time.get_ticks()
        decorridos_ticks = agora - self.last_poder

        #Verifica se pode atirar novamente
        if decorridos_ticks > self.pooder_ticks:
            self.last_poder = agora
            new_poder = Poderzin(self.assets, Boss.rect)
            self.groups['all_sprites'].add(new_poder)
            self.groups['all_poderzin'].add(new_poder)

#Classe que representa o poder do Boss
class Poderzin(pygame.sprite.Sprite):
    def __init__(self, assets, chefão):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[PODER_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = chefão.rect.left
        self.rect.y = chefão.rect.centery
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)
        self.chefão = chefão

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.top > altura_janela) or (self.rect.right < 0) or (self.rect.left > largura_janela):
            self.rect.x = self.chefão.rect.left 
            self.rect.y = self.chefão.rect.centery
            self.speedx = random.randint(-5, 5)
            self.speedy = random.randint(2, 5)

# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, centery, left):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BULLET_IMG]
        self.rect = self.image.get_rect()
        
        self.rect.left = left
        self.rect.centery = centery-25
        self.speedx = velo_tiro
    
    def update(self):
        self.rect.x += self.speedx

        if self.rect.left > largura_janela or self.rect.right < 0:
            self.kill()


