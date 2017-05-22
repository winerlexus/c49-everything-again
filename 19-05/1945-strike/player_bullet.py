import pygame
from player import *
class PlayerBullet: # -*- coding: utf-8 -*-
    def __init__(self,x,y):
        self.type = "bullet" 
        self.image = pygame.image.load("resources/bullet-single.png")
        self.x= x - self.image.get_width()/2
        self.y= y - self.image.get_height()/2 
        

    def run(self):
        self.y -= 10
        
    
    def draw(self,screen):
        screen.blit(self.image, (self.x ,self.y))

