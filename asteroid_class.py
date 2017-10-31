from pygame.sprite import Sprite
import pygame


class Asteroid(Sprite):
    def __init__(self, screen, width, height, speedx, startx, starty):
        Sprite.__init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = speedx

        self.image = pygame.image.load("meteor.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.screen = screen

    def movement(self):
        self.rect.left -= self.speedx





