# -*- coding: utf-8 -*-
import pygame
from input_manager import *
from GM import *
from player_bullet import *
class Player:
    def __init__(self):
        self.image = pygame.image.load("resources/plane3.png")
        self.type = "player"
        self.x = 0 - self.image.get_width()/2
        self.y = 0 -self.image.get_height()/2                            
    
    def draw(self,screen):
        screen.blit(self.image,\
                    (self.x ,self.y))
        
    def run(self):
        if input_manager.rightpress:
            self.x +=3
        if input_manager.uppress:
            self.y -=3
        if input_manager.leftpress:
            self.x -=3
        if input_manager.downpress:
            self.y +=3
        if input_manager.space:
            player_bullet = PlayerBullet(self.x + self.image.get_width()/2 ,self.y)
            game_manager.add(player_bullet)

player1 = Player()
