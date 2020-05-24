import pygame

pygame.init()

# Variáveis
largura_janela = 1080
altura_janela = 540
largura_background = 1080
altura_background = 540
largura_mario = 64
altura_mario = 64
gravidade = 2
tamanho_pulo = 10
altura_chão = altura_janela - 60
TITULO = 'Mariozinho'

# Possíveis estados do jogador
STILL = 0
JUMPING = 1
FALLING = 2

#Janela
window = pygame.display.set_mode((largura_janela,altura_janela))
pygame.display.set_caption(TITULO)

#assets
background = pygame.image.load('assets/img/mario_backgroud.png').convert()
background = pygame.transform.scale(background,(largura_background,altura_background))
mario_img = pygame.image.load('assets/img/nego_mario.png').convert_alpha()
mario_img = pygame.transform.scale(mario_img,(largura_mario,altura_mario))

#Classe Personagem que representa o herói
class Personagem(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 64 
        self.rect.bottom = altura_janela - 32
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


PLAYING = 0
DONE = 1

clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()

player = Personagem(mario_img)
all_sprites.add(player)

state = PLAYING
while state != DONE:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state = DONE

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx -= 1
            if event.key == pygame.K_RIGHT:
                player.speedx += 1
            if event.key == pygame.K_UP:
                player.pulo()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedx += 1
            if event.key == pygame.K_RIGHT:
                player.speedx -= 1
        
    
    all_sprites.update()

    window.fill((46, 139, 87))
    window.blit(background,(0,0))
    
    all_sprites.draw(window)
    #all_sprites.display.flip()

    pygame.display.update()

#try:
#    game_screen(window)
#finally:
#    pygame.quit()
pygame.quit()