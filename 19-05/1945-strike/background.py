# -*- coding: utf-8 -*-

import pygame

class Background:
    def __init__(self):
        self.type = "background"
        self.image = pygame.image.load("resources/background.png")
        self.y = 0
        self.y2 = -self.image.get_height()
    
    def draw(self, screen):
        screen.blit(self.image, (0,self.y))
        screen.blit(self.image, (0,self.y2))
    
    def run(self):
        self.y2 += 5
        self.y +=5
        
        if self.y2 >=0 :
            self.y2 =-self.image.get_height()
            self.y = 0
        