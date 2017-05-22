# -*- coding: utf-8 -*-
import enemies
import player_bullet
class GameManager:
    def __init__(self):
        self.game_objects = []
        
        self.enemies = []
        
        self.bullets = []
        
        
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
            game_object.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def remove(self,game_object):       
        #bullet not penetrate 
        if game_object.type == "bullet":
            self.bullet.remove(game_object)
        if game_object.type == "enemy":
            self.enemies.remove(game_object)
    
    def check_hit(self):
        for bullet in game_manager.bullets :
            for enemy in game_manager.enemies:
                print(enemy)
                if bullet.x >= enemy.x - enemy.image.get_width()/2 and bullet.x<= enemy.x + enemy.image.get_width()/2\
                    and bullet.y <= enemy.y + enemy.image.get_height()/2:
                        game_manager.remove(self.bullets.bullet)
                        enemy.alive = False
    
    def cleanup(self):
        for enemy in gamemanager.enemies:
            if enemy.alive == False:
                gamemanager.remover(enemy)                   
                                                                                     
game_manager = GameManager()