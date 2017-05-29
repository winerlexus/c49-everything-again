# -*- coding: utf-8 -*-
import pygame

class Input_manager:
    def __init__(self):
        self.rightpress = False
        self.leftpress = False
        self.uppress = False
        self.downpress = False
        self.space =False
        
    def run(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.rightpress = True
                if event.key == pygame.K_UP:
                    self.uppress = True
                if event.key == pygame.K_LEFT:
                    self.leftpress = True
                if event.key == pygame.K_DOWN:
                    self.downpress = True
                if event.key == pygame.K_SPACE:
                    self.space = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rightpress = False
                if event.key == pygame.K_UP:
                    self.uppress = False
                if event.key == pygame.K_LEFT:
                    self.leftpress = False
                if event.key == pygame.K_DOWN:
                    self.downpress = False
                if event.key == pygame.K_SPACE:
                    self.space = False

input_manager = Input_manager()