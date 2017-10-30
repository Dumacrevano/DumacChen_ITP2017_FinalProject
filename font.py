import pygame
from pygame import *


class Word:

    def __init__(self,screen, position_x, position_y, text):
        pygame.font.init()
        self.font = pygame.font.SysFont("times new roman",40)
        self.position_x = position_x
        self.position_y = position_y
        self.text = text
        self.screen = screen

    def update(self):
        self.text_surface=self.font.render(self.text , True , (255, 255, 255))
        self.screen.blit(self.text_surface,(self.position_x,self.position_y))
        pygame.display.flip()