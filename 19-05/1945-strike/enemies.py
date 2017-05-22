import pygame# -*- coding: utf-8 -*-
from player import * 
from GM import *
from player_bullet import *


class Enemy_type1:
    def __init__(self):
        self.type = "enemy"
        self.image = pygame.image.load("resources/enemy_plane_yellow_1.png")
        self.x = 300 - self.image.get_width()/2
        self.y = -20 - self.image.get_height()/2
        self.alive = True
        
    def draw(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x ,self.y))
        
    def run(self):
        self.y += +1 
     
    
enemy_type1 = Enemy_type1()
       
        