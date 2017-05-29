import pygame
from player import *
from points import *
class Enemy_bullet: # -*- coding: utf-8 -*-
    def __init__(self,x,y):
        self.type = "bullet" 
        self.image = pygame.image.load("resources/bullet-single.png")
        self.position =  Position()
        self.position.x= x - self.image.get_width()/2
        self.position.y= y - self.image.get_height()/2 
      

    def run(self):
        self.position.add_up(0,-20)
        
    
    def draw(self,screen):
        screen.blit(self.image, (self.position.x ,self.position.y))

enemy_bullet = Enemy_bullet