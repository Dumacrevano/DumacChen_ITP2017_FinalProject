import pygame
from pygame import *
screen_colour=(255,255,255)

class button():
    def __init__(self,image):
        self.image=pygame.load(image)
        self.rect=self.image.get_rect()

screen=pygame.display.set_mode([600,600])
pygame.display.set_caption("hello","hello")
pygame.init()
pause=True
while pause:

    screen.fill(screen_colour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            pause=False
    pygame.display.update()