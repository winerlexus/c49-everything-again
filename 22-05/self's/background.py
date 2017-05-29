# -*- coding: utf-8 -*-

import pygame
from points import *
from renderer import *
class Background:
    def __init__(self):
        self.type = "background"
       
    
        self.renderer = ImageRenderer(pygame.image.load("resources/background.png"))
        self.position = Point()
        self.position.x = -self.renderer.width/2
        
        self.position.y = 0
        self.position.y2 = self.renderer.height
    
    def run(self):
        self.position.y2 += 5
        self.position.y += 5
        
        if self.position.y2 >=0 :
            self.position.y2 =-self.renderer.height
            self.position.y = 0
        