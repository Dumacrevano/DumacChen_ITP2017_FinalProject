import sys, pygame

from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    def __init__(self,screen, startx, starty):
        Sprite. __init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = 20

        self.image = pygame.image.load("bullets.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.rect.center = (startx,starty)
        self.screen = screen
    def movement(self):
        #self.screen.blit(self.image,[self.startx,self.starty])
        self.rect.left += self.speedx

