# -*- coding: utf-8 -*-
import pygame
from input_manager import *
from GM import *
from player_bullet import *
from points import *
from renderer import *
class Player:
    def __init__(self):
        self.type = "player"
        self.position = Point()
        self.renderer = load_renderer("resources/plane3.png")
        self.position.x = 400
        self.position.y = 500                             
        self.cool_down_period = 10
        self.cool_down_counter = 0
        self.shoot_disable = False
        self.constraints = None

        
    def run(self):
        self.move()
        self.shoot()
        
    def move(self):
        if input_manager.rightpress:
            self.position.add_up(5,0)
        if input_manager.uppress:
            self.position.add_up(0,-5)
        if input_manager.leftpress:
            self.position.add_up(-5,0)
        if input_manager.downpress:
            self.position.add_up(0,5)
#        if self.constraints is not None:
#            self.constraints.make(self.position)
#        self.x = max(self.x,0)
#        self.x = min(self.x,600-self.image.get_width())
#        self.y = max (self.y,0)
#        self.y = min (self.y, 800-self.image.get_height()*2)
    def shoot(self):
        if self.shoot_disable :   #cooled down
            self.cool_down_counter += 1
            if self.cool_down_counter >= 10:
                self.cool_down_counter = 0
                self.shoot_disable = False
            return #return stop all following components
        if input_manager.space:
            player_bullet = PlayerBullet(self.position.x + self.image.get_width()/2 ,self.position.y)
            game_manager.add(player_bullet)
            self.shoot_disable = True
player1 = Player()