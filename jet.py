import bullet
from pygame import *
from pygame.sprite import *

class Jet(Sprite):
    """initialize the jet"""

    def __init__(self, screen):
        Sprite.__init__(self)
        self.image = image.load("battlejet.png")
        self.image = pygame.transform.scale(self.image, (90, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 50
        self.screen = screen
        self.shoot_flag = False
        self.move_speed = 6
        """bullet !"""
        self.bullets = []
        self.firerates = 2

    def moveleft(self):
        self.rect.x -= self.move_speed
        display.flip()

    def moveright(self):
        self.rect.x += self.move_speed
        display.flip()

    def moveup(self):
        self.rect.y -= self.move_speed
        display.flip()

    def movedown(self):
        self.rect.y += self.move_speed
        display.flip()

    #def shoot(self):
        """method for shooting"""
        #bullet.bullet(self.rect.x, self.rect.y, self.bullets, self.screen, 40)