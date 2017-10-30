import pygame as pg
from pygame import *

class Star:
    #resourse of the backgound setting
    def __init__(self):
        self.background=image.load("star.gif")
        self.background=pg.transform.scale(self.background,(800,600))
        self.background_size=self.background.get_size()
        self.background_rect=self.background.get_rect()
        self.width,self.height=self.background_size
