import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        BLACK = (0, 0, 0)
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height]) 

        self.velocity = [3, 3] #pixels per frame

        self.rect = self.image.get_rect()

    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y
        
    def move(self):
         self.rect.y += self.velocity[1]    

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[0] = random.randint(-3, 3)

    def reset_pos(self):
        self.rect.x = 345
        self.rect.y = 195
        self.velocity = [0, 0]