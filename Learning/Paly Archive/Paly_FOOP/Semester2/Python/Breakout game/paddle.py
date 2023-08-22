import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        BLACK = (0, 0, 0)
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
    

    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        pass

    def bounce(self):
        pass

    def reset_pos(self):
        pass
    
    def left(self, amount):
        self.rect.x -= amount

    def right(self, amount):
        self.rect.x += amount