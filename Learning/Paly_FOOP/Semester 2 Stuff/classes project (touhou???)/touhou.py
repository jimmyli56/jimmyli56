#touhou in python with classes 
#importing modules
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

#classes needed
#player
#bullet
#enemy
#powerup
#background
#score

pygame.init()

#screen size
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Touhou")

#background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

#player
player = pygame.image.load("player.png").convert()
player.set_colorkey((0, 0, 0))
playerpos = [320, 240]

#bullet
bullet = pygame.image.load("bullet.png").convert()
bullet.set_colorkey((0, 0, 0))
bullets = []

#enemy
enemy = pygame.image.load("enemy.png").convert()
enemy.set_colorkey((0, 0, 0))
enemies = [[640, 100]]

#game loop
while 1:
    #clear screen
    screen.blit(background, (0, 0))
    
    #player movement
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32), position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)
    
    #bullet movement
    for bullet in bullets:
        index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            bullets.pop(index)
        index += 1
        for projectile in bullets:
            bullet1 = pygame.transform.rotate(bullet, 360-projectile[0]*57.29)
            screen.blit(bullet1, (projectile[1], projectile[2]))
            
    #enemy movement
    if random.random() > 0.95:
        enemies.append([640, random.randint(50, 430)])
    index = 0
    for enemy in enemies:
        if enemy[0] < -64:
            enemies.pop(index)
        enemy[0] -= 5
        
        #collision
        enemyrect = pygame.Rect(enemyimg.get_rect())
        enemyrect.top = enemy[1]
        enemyrect.left = enemy[0]
        if enemyrect.left < playerpos[0] + 64:
            hit.play()
            enemies.pop(index)
        index += 1
        for enemy in enemies:
            screen.blit(enemyimg, enemy)
            
    #update screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            bullets.append([math.atan2(position[1])])-(playerpos1[1]+32), position
