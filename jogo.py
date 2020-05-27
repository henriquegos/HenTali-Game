#importa bibliotecas necessarias
import pygame
import random

#inicia framework
pygame.init()

# Variáveis
largura_janela = 1080
altura_janela = 540
largura_background = 1080
altura_background = 540
largura_heroi = 80
altura_heroi = 80
largura_tiro = 160
altura_tiro = 80
largura_boss = 160
altura_boss = 160
largura_poderzin = 40
altura_poderzin = 40
gravidade = 2
tamanho_pulo = 30
altura_chão = altura_janela - 45
velo_tiro = 5
SPEEDX = 3
FPS = 60
TITULO = 'Mariozinho'

# Possíveis estados do jogador
STILL = 0
JUMPING = 1
FALLING = 2

#Janela
window = pygame.display.set_mode((largura_janela,altura_janela))
pygame.display.set_caption(TITULO)

#assets
def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('assets/img/mario_backgroud.png').convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'],(largura_background,altura_background))
    assets['mario_img'] = pygame.image.load('assets/img/nego_mario.png').convert_alpha()
    assets['mario_img'] = pygame.transform.scale(assets['mario_img'],(largura_heroi,altura_heroi))
    assets['bullet_img'] = pygame.image.load('assets/img/mario_especial.png').convert_alpha()
    assets['bullet_img'] = pygame.transform.scale(assets['bullet_img'],(largura_tiro,altura_tiro))
    assets['boss_img'] = pygame.image.load('assets/img/boss_mario.png').convert_alpha()
    assets['boss_img'] = pygame.transform.scale(assets['boss_img'],(largura_boss, altura_boss))
    assets['poder_img'] = pygame.image.load('assets/img/poder_boss.png').convert_alpha()
    assets['poder_img'] = pygame.transform.scale(assets['poder_img'], (largura_poderzin, altura_poderzin))
    return assets

#Classe Personagem que representa o herói
class Personagem(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['mario_img']
        self.rect = self.image.get_rect()
        self.rect.centerx = 64 
        self.rect.bottom = altura_chão
        self.groups = groups
        self.assets = assets
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

        self.image = assets['boss_img']
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
            self.groups = groups
            self.assets = assets


    # Responsável pelo poderzinho do Chefão
    def poder(self):
        agora = pygame.time.get_ticks()
        decorridos_ticks = agora - self.last_poder

        #Verifica se pode atirar novamente
        if decorridos_ticks > self.pooder_ticks:
            self.last_poder = agora
            new_poder = Poderzin(self.assets, self.rect.centery, self.rect.right)
            self.groups['all_sprites'].add(new_poder)
            self.groups['all_poderzin'].add(new_poder)

#Classe que representa o poder do Boss
class Poderzin(pygame.sprite.Sprite):
    def __init__(self, assets, centery, left):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['poder_img']
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = centery
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.top > altura_janela) or (self.rect.right < 0) or (self.rect.left > largura_janela):
            self.rect.x = chefão.rect.left
            self.rect.y = chefão.rect.centery
            self.speedx = random.randint(-5, 5)
            self.speedy = random.randint(2, 5)

# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, centery, left):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bullet_img']
        self.rect = self.image.get_rect()
        
        self.rect.left = left
        self.rect.centery = centery-25
        self.speedx = velo_tiro
    
    def update(self):
        self.rect.x += self.speedx

        if self.rect.left > largura_janela or self.rect.right < 0:
            self.kill()

PLAYING = 0
DONE = 1

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
    poder = Poderzin(assets, chefão.rect.centery, chefão.rect.left)
    all_sprites.add(poder)
    all_poderzin.add(poder)

# ======== Loop principal =========
state = PLAYING
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

pygame.quit()