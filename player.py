import pygame
from pygame.locals import *

vec = pygame.math.Vector2
GRAV = 6.5
FRIC = -.12

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, jumpforce):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((128, 40, 40))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.pos = vec((x, y))
        self.vel = vec(0, 0)
        self.acc = vec(0, GRAV)

        self.jumpforce = jumpforce
        self.canjump = False 
        self.speed = speed 

    def update(self):
        self.horizontal_movement()
        self.vertical_movement()

    def horizontal_movement(self):
        self.acc = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_LEFT]:
            self.acc.x = -self.speed
        if pressed_keys[K_RIGHT]:
            self.acc.x = self.speed
        if pressed_keys[K_SPACE] and self.canjump:
            self.acc.y = self.jumpforce - self.jumpforce * 2
            self.acc.x = 0
            self.canjump = False

        self.acc.x += self.vel.x * FRIC
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + (0.5 * self.acc.x)

        self.limit_vel(4)

        self.rect.x = self.pos.x ##rect.get_height()
    
    def vertical_movement(self):
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + (self.acc.y * 0.5)

        if self.pos.y > 590:
            self.on_ground = True
            self.vel.y = 0
            self.pos.y = 590 + self.rect.get_height() # confia

    def limit_vel(self, max_vel):
        self.vel.x = max(-max_vel, min(self.vel.x, max_vel))
        if abs(self.vel.x) < .01: 
            self.vel.x = 0 
