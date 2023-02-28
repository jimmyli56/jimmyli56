# classic breakout game
import pygame
from pygame.locals import *
import paddle
import ball
import brick
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

#add bricks to screen

for i in range(7):
    bricks = brick.Brick(PERIWINKLE, 80, 30)
    bricks.setxy(60 + i * 100, 60)
    all_sprites_list.add(bricks)
    all_bricks.add(bricks)
    pass

# add another row of bricks
for i in range(7):
    bricks = brick.Brick(PERIWINKLE, 80, 30)
    bricks.setxy(60 + i * 100, 100)
    all_sprites_list.add(bricks)
    all_bricks.add(bricks)
    pass

for i in range(7):
    bricks = brick.Brick(PERIWINKLE, 80, 30)
    bricks.setxy(60 + i * 100, 140)
    all_sprites_list.add(bricks)
    all_bricks.add(bricks)
    pass

for i in range(7):
    bricks = brick.Brick(PERIWINKLE, 80, 30)
    bricks.setxy(60 + i * 100, 180)
    all_sprites_list.add(bricks)
    all_bricks.add(bricks)
    pass

#add paddles and ball to screen
paddle1 = paddle.Paddle(WHITE, 100, 10)
paddle1.setxy(350,560)

all_sprites_list.add(paddle1)

ball1 = ball.Ball(WHITE, 10, 10)
ball1.setxy(400, 510)

all_sprites_list.add(ball1)


#game loop

playing = True

clock = pygame.time.Clock()
while playing:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    paddle1.left(10)
  #now right or you can use other keys too 
  if keys[pygame.K_RIGHT]:
    paddle1.right(10)
  all_sprites_list.update()
  
  #bounce off sides
  if ball1.rect.y>590:
    ball1.velocity[1] = -ball1.velocity[1]
    #went below paddle
    lives -= 1
    pygame.time.wait(2000)
    ball1.setxy(400, 540)
  
  #wall bounce
  if ball1.rect.x>790:
    ball1.velocity[0] = -ball1.velocity[0]
  if ball1.rect.x<0:
    ball1.velocity[0] = -ball1.velocity[0]
  #ceiling bounce
  if ball1.rect.y<40:
    ball1.velocity[1] = -ball1.velocity[1]

  
  #paddle limits
  if paddle1.rect.x<0:
    paddle1.rect.x=0
  if paddle1.rect.x>700:
    paddle1.rect.x=700

  if pygame.sprite.collide_mask(ball1, paddle1):
    #depending on how bounce is made, update accordingly
    ball1.rect.x -= ball1.velocity[0]
    ball1.bounce()
  
  brick_collision_list = pygame.sprite.spritecollide(ball1, all_bricks, False)
  for bricks in brick_collision_list:
    ball1.bounce()
    bricks.kill()
    #increase score
    score += 1
    #if no more bricks
    if len(all_bricks) == 0:
      playing=False
      
  screen.fill(BLACK)
  pygame.draw.line(screen, WHITE, [0,38],[800,38],2)
  
  text = pygame.font.Font(None, 34).render("Score: " + str(score), 1, WHITE)
  screen.blit(text, (20,10))
  
  text = pygame.font.Font(None, 34).render("Lives: " + str(lives), 1, WHITE)
  screen.blit(text, (650,10))

#kill game if no lives left
  if lives == 0:
    playing = False

  all_sprites_list.draw(screen)

  pygame.display.flip()

  clock.tick(60)
 


pygame.quit()