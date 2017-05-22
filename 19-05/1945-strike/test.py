# -*- coding: utf-8 -*-
"""
Created on Fri May 19 20:03:40 2017

@author: Administrator
"""

import pygame
from player import *
from background import*
from input_manager import *
from GM import *
from enemies import *

loop = True

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption('Bắn máy bay cực mạnh - by techkids')
    return screen


def run():
    game_manager.run()

def draw(screen):
    screen.fill((0,0,0))
    
    game_manager.draw(screen)

def handle_exit_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            return False
    return True
screen = init_pygame()
clock = pygame.time.Clock()

game_manager.add(Background())
game_manager.add(Player())
game_manager.add(Enemy_type1())
               
while loop:
        ## update logic
        events = pygame.event.get() ## get only once per loop
        loop = handle_exit_events(events)
        input_manager.run(events)
        run()
        
        ## update graphics
        draw(screen)
        
        ## delay by frame rate
        pygame.display.flip()
        clock.tick(20)
pygame.quit()