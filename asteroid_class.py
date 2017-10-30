from pygame.sprite import Sprite
import pygame
class Asteroid(Sprite):
    def __init__(self,screen,width,height,speedx,startx,starty):
        Sprite. __init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = speedx

        self.image = pygame.image.load("meteor.png")
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect=self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.screen=screen
    def movement(self):
        #self.screen.blit(self.image,[self.startx,self.starty])
        self.rect.left -= self.speedx



class Asteroid_2(Asteroid):
    """initialize another asteroid as obstacle"""
    def __init__(self,screen,width,height,speedx,startx,starty):
        super(Asteroid_2, self).__init__(screen,width,height,speedx,startx,starty)
        self.startx = startx
        self.starty = starty

        self.speedx = speedx

        self.image = pygame.image.load("asteroid_2.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty


"""class asteroid_3(Asteroid):
    def __init__(self,screen,widht,height,speedx,speedy,startx,starty):
        super(asteroid_3, self).__init__(screen,widht,height,speedx,speedy,startx,starty)
        self.width=widht
        self.height=height
        self.speedx=speedx
        self.speedy=speedy
        self.image=pygame.image.load("asteroid_2.png")
        self.rect = self.image.get_rect()
        self.screen=screen"""