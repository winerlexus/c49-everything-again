import pygame# -*- coding: utf-8 -*-
class Point():
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def add_up(self,dx,dy):
        self.x += dx
        self.y += dy
        
    def add(self,dx,dy):
        p = Point()
        p.x = self.x + dx
        p.y = self.y + dy
        return p
    
    def copy(self,other):
        self.x = other.x
        self.y = other.y