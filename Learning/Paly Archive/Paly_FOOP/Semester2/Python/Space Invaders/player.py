import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.image = pygame.image.load("player.png")

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
