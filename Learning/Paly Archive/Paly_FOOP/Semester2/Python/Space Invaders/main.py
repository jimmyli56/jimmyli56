import pygame
import enemies
import player
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PERIWINKLE = (204, 204, 255)

# globals
score = 0
lives = 3

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breakout Game")

#set groups
all_sprites_list = pygame.sprite.Group()
all_bricks = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    for enemy in enemies:
        if enemy.collide(player):
            print("Game Over")
            pygame.quit()
            sys.exit()
        if enemy.x < 0:
            enemy.move_right()
        elif enemy.x + enemy.width > 600:
            enemy.move_left()

    screen.fill((0, 0, 0))
    screen.blit(player.image, (player.x, player.y))
    for enemy in enemies:
        screen.blit(enemy.image, (enemy.x, enemy.y))
    pygame.display.update()
