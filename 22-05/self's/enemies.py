import pygame# -*- coding: utf-8 -*-
from player import * 
from GM import *
from player_bullet import *
from points import *
from renderer import *
from physics import *
class Enemy:
    def __init__(self):
        self.type = "enemy"
        self.position = Point()
        self.renderer = load_renderer("resources/enemy_plane_yellow_1.png")
        self.position.x = 300 
        self.position.y = -20 
        self.alive = True
        self.box_collider = BoxCollider(self.position,self.renderer.width,self.renderer.height)
        physic.add(self)
    def run(self):
        self.position.add_up(0,1)
        if self.position.y >= 300:
            self.position.add_up(2,0)
        
#    def shoot(self):
#        
enemy_type1 = Enemy()
       
        