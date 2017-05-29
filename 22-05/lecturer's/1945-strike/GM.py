# -*- coding: utf-8 -*-
import enemies
from player_bullet import *
from points import *
class GameManager:
    def __init__(self):
        self.game_objects = []
        
        self.enemies = []
        
        self.bullets = []
        
        self.position = Point()
        self.position.x = 0
        self.position.y = 0
    def add(self,game_object):
        if game_object.type == "enemy" :
            self.enemies.append(game_object)
        
        if game_object.type == "bullet":
            self.bullets.append(game_object)
        
        else :
            self.game_objects.append(game_object)
        
        
    def run(self):
        for game_object in self.game_objects:
            game_object.run()
        for bullet in self.bullets:
            bullet.run()
        for enemy in self.enemies:
            enemy.run()
   
    def draw(self,screen):
        for game_object in self.game_objects:
            game_object.renderer.draw(screen,game_object.position)
        for bullet in self.bullets:
            bullet.renderer.draw(screen,bullet.position)
        for enemy in self.enemies:
            enemy.position.draw(screen,enemy.position)
            
    def remove(self,game_object):       
        #bullet not penetrate 
        if game_object.type == "bullet":
            self.bullets.remove(game_object)
        if game_object.type == "enemy":
            self.enemies.remove(game_object)
    
    def check_hit(self):
        for enemy in game_manager.enemies:
            for bullet in game_manager.bullets :
                if bullet.position.y < 0 or bullet.position.y>800:
                    game_manager.remove(bullet)
                if bullet.position.x >= enemy.position.x  and bullet.position.x<= enemy.position.x + enemy.image.get_width()\
                        and bullet.position.y <= enemy.position.y + enemy.image.get_height()/2:
                            game_manager.remove(bullet)
                            enemy.alive = False
                            if enemy.alive == False:
                                game_manager.remove(enemy)

    def generate_enemy(self):
        first_enemy = enemies.Enemy_type1()
        game_manager.add(first_enemy)
#    def cleanup(self):
#        for enemy in game_manager.enemies:
#            if enemy.alive == False:
#                game_manager.remove(enemy)
#        for bullet in game_manager.bullets:
#            if bullet.y < 0 or bullet.y > 800:
#                game_manager.remove(bullet)           
#                                                                                     
game_manager = GameManager()