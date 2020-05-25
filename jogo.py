import pygame

pygame.init()

# Variáveis
largura_janela = 1080
altura_janela = 540
largura_background = 1080
altura_background = 540
largura_mario = 80
altura_mario = 80
largura_tiro = 160
altura_tiro = 80
gravidade = 2
tamanho_pulo = 20
altura_chão = altura_janela - 45
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
    assets['mario_img'] = pygame.transform.scale(assets['mario_img'],(largura_mario,altura_mario))
    assets['bullet_img'] = pygame.image.load('assets/img/mario_especial.png').convert_alpha()
    assets['bullet_img'] = pygame.transform.scale(assets['bullet_img'],(largura_tiro,altura_tiro))
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
    
    def pulo(self):
        if self.state == STILL:
            self.speedy -= tamanho_pulo
            self.state = JUMPING
    
    def shoot(self):
        new_bullet = Bullet(self.assets, self.rect.centery, self.rect.left)
        self.groups['all_sprites'].add(new_bullet)
        self.groups['all_bullets'].add(new_bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, centery, left):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bullet_img']
        self.rect = self.image.get_rect()
        
        self.rect.left = left
        self.rect.centery = centery-25
        self.speedx = 2
    
    def update(self):
        self.rect.x += self.speedx

        if self.rect.left > largura_janela or self.rect.right < 0:
            self.kill()

PLAYING = 0
DONE = 1

clock = pygame.time.Clock()
assets = load_assets()

all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_bullets'] = all_bullets

player = Personagem(groups, assets)
all_sprites.add(player)

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
        
    
    all_sprites.update()

    window.fill((46, 139, 87))
    window.blit(assets['background'],(0,0))
    
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()