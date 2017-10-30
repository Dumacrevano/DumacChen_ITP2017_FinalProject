from pygame import *

from pygame.sprite import *
from jet import Jet

import menu
from back_ground import Star

from asteroid_class import *

from bullet import Bullet
import random


class Button(Sprite):
    """initialize the button"""
    def __init__(self,image):
        Sprite. __init__(self)
        self.button=pygame.image.load(image)
        self.button=pygame.transform.scale(self.button,(300,150))


def run_game():
    """function to move the background image"""
    scores = 0
    theClock = pygame.time.Clock()
    bg_image = Star()
    background = bg_image.background
    x = 0
    y = 0

    x1 = bg_image.width
    y1 = 0

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    display.set_caption("Jet mission")

    #creating a jet
    jet1 = Jet(screen)
    all_sprites = Group(jet1)

    #create asteroid object group
    asteroid_group=Group()

    #create bullets object Group
    bullets=Group()



    time = 40
    asteroid_timer = pygame.time.get_ticks()
    while True:
        time += 0.005
        """background move"""
        theClock.tick(time)
        x -= 5
        x1 -= 5
        screen.blit(background, (x, y))
        screen.blit(background, (x1, y1))
        if x < -bg_image.width:
            x = 0
        if x1 < 0:
            x1 = bg_image.width

        # create score board
        font=pygame.font.SysFont("Times New Romans",36)
        score_board=font.render("score:"+str(scores),True,(255,255,255))
        # update refered to the word's method
        screen.blit(score_board,(10,550))



        all_sprites.draw(screen)

        bullets.draw(screen)

        asteroid_group.draw(screen)
        display.update()#update jet and screen view

        event.get()
        """moving the jet according to key pressed"""

        key = pygame.key.get_pressed()
        if key[K_LEFT] and jet1.rect.x>0:
            jet1.moveleft()

        if key[K_RIGHT] and jet1.rect.x<=700:
            jet1.moveright()

        if key[K_DOWN] and jet1.rect.y<=500:
            jet1.movedown()

        if key[K_UP] and jet1.rect.y>0:
            jet1.moveup()

        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/20000):
            bullet = Bullet(screen, jet1.rect.x+50, jet1.rect.y+42)
            bullets.add(bullet)

        if key[K_ESCAPE]:
            menu.menu_screen(Button,run_game)

        if key[K_p]:
            menu.pause_menu(Button,run_game)


        """generate asteroid randomly"""
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            asteroid = Asteroid(screen, 50, 50, 10, 1000, (random.randint(1,18) * 30))
            asteroid_group.add(asteroid)
            asteroid_timer = pygame.time.get_ticks()

        """update the movement of asteroid"""
        for asteroid in asteroid_group:
            asteroid.movement()
            if asteroid.rect.right <= 0:
                asteroid_group.remove(asteroid)
            groupcollide(all_sprites,asteroid_group,dokilla=True,dokillb=True)

        """update bullet movement on screen"""
        for bullet in bullets:
            bullet.movement()
            if bullet.rect.left>800:
                bullets.remove(bullet)
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):
                scores += 100

menu.menu_screen(Button,run_game)

