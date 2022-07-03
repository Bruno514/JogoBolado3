import pygame,os
# para corno pq vc faz cagada
# fodase
# nn foco agora
# foco
from player import Player
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2


H = 600
W = 600
FPS = 60

green = (0, 255, 0)
blue = (0, 0, 128)

clock = pygame.time.Clock()  # tem q ser diferente do fps la de cima
display = pygame.display.set_mode((W, H), pygame.RESIZABLE)

pygame.display.set_caption("A HISTORIA DA PULGA")
font = pygame.font.Font("freesansbold.ttf", 32)

text = font.render("Historia da Pulga", True, green, blue)


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((W + 50, 20))
        self.image.fill((124, 252, 0))
        self.rect = self.image.get_rect(center=(W / 2, H - 10))

    def update(self):   
        pass


def check_collision(player, platform):
    if player.rect.colliderect(platform.rect):
        player.rect.bottom = platform.rect.top + 1
        player.pos = player.rect.midbottom
        player.vel.y = 0
        player.acc.x = 0
        if player.canjump == False:
            player.vel.x = 0
            player.canjump = True

P1 = Player(x=5, y=5, speed=2, jumpforce=12)
PT1 = Platform()

# corno

print(P1.rect.x , P1.rect.y)
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    display.fill((0, 181, 226))

    all_sprites.update() 
    check_collision(player=P1, platform=PT1)
    print("ACCx: " + str(P1.acc.x))
    print("VELx: " + str(P1.vel.x))

    all_sprites.draw(display)  
    pygame.display.flip()  
    clock.tick(FPS)  

    
