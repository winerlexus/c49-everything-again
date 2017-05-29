# -*- coding: utf-8 -*-
import pygame
from player import *
from points import *
class Constraints:
    def __init__(self,min_x,max_x,min_y,max_y,player1):
        self.min_x = min_x 
        self.min_y = min_y
        self.max_x = max_x - player1.image.get_width()
        self.max_y = max_y - player1.image.get_height()
        
    def clamp(self,value,min_value,max_value):
        value = min(value,max_value)
        value = max(value,min_value)
        
        return value
    def make(self,x,y):
        position.x = self.clamp(x,self.min_x,self.max_x)
        position.y = self.clamp(y,self.min_y,self.max_y)

