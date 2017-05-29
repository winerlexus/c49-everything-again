import pygame
from player import *
from points import *
from boxcollider import *
from physics import *
class PlayerBullet: # -*- coding: utf-8 -*-
    def __init__(self,x,y):
        self.type = "bullet" 
        self.renderer = ImageRenderer("resources/bullet-single.png")
        self.position = Point()
        self.position.x= x - self.renderer.width/2
        self.position.y= y - self.renderer.height/2 
        self.box_collider = BoxCollider(self.position,self.renderer.width,self.renderer.height)
      

    def run(self):
        self.position.add_up(0,-20)
        target = physics.check_contact(self.box_collider)
        if target is not None and target is Enemy:
        
    
    def draw(self,screen):
        screen.blit(self.image, (self.position.x ,self.position.y))

