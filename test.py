import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

bullets=[]

background = pygame.image.load("star.gif")
background=pygame.transform.scale(background,(800,600))
ship = pygame.image.load("battlejet.png")
ship = pygame.transform.scale(ship,(125,70))
bulletpicture = pygame.image.load("bullets.png")
bulletpicture = pygame.transform.scale(bulletpicture,(50,50))
bullets_flag=True



while True:

  clock.tick(60)

  mx,my = pygame.mouse.get_pos()
  pygame.mouse.set_visible(False)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    elif event.type == MOUSEBUTTONDOWN:
      bullets_flag=True
      if bullets_flag:
        bullets.append([event.pos[0] - 32, my + 25])

    elif event.type == MOUSEBUTTONUP:
      bullets_flag=False

  for b in range(len(bullets)):
    bullets[b][0]+=20

  for bullet in bullets:
    if bullet[0]>800:
      bullets.remove(bullet)

  screen.blit(background,(0,0))

  for bullet in bullets:
    screen.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))

  screen.blit(ship,(mx-20,my-20))
  pygame.display.flip()
  print(len(bullets))