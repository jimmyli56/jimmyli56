import pygame
from pygame.locals import *
import sys
import random
import math
import time
import os
import copy
import pickle
import pygame.mixer
import pygame.font
import pygame.image
import pygame.transform
import pygame.draw
import pygame.event
import pygame.time
import pygame.display
import pygame.sprite
import pygame.key
import pygame.mouse
import pygame.joystick
import pygame.color
import pygame.surface

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.speed = 5
        self.shoot_delay = 0
        self.health = 100
        self.shoot_delay = 0
        self.shoot_delay2 = 0
        self.shoot_delay3 = 0
        self.shoot_delay4 = 0
        self.shoot_delay5 = 0
        self.shoot_delay6 = 0
        self.shoot_delay7 = 0
        self.shoot_delay8 = 0
        self.shoot_delay9 = 0
        self.shoot_delay10 = 0
        self.shoot_delay11 = 0
        self.shoot_delay12 = 0
        self.shoot_delay13 = 0
        self.shoot_delay14 = 0
        self.shoot_delay15 = 0
        self.shoot_delay16 = 0
        self.shoot_delay17 = 0
        self.shoot_delay18 = 0
        self.shoot_delay19 = 0
        self.shoot_delay20 = 0
        self.shoot_delay21 = 0
        self.shoot_delay22 = 0
        self.shoot_delay23 = 0
        self.shoot_delay24 = 0
        self.shoot_delay25 = 0
        self.shoot_delay26 = 0
        self.shoot_delay27 = 0
        self.shoot_delay28 = 0
        self.shoot_delay29 = 0
        self.shoot_delay30 = 0
        self.shoot_delay31 = 0
        self.shoot_delay32 = 0
        self.shoot_delay33 = 0
        self.shoot_delay34 = 0
        self.shoot_delay35 = 0
        self.shoot_delay36 = 0
        self.shoot_delay37 = 0
        self.shoot_delay38 = 0
        self.shoot_delay39 = 0
        self.shoot_delay40 = 0
        self.shoot_delay41 = 0
        self.shoot_delay42 = 0
        self.shoot_delay43 = 0
        