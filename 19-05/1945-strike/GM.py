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
            self.bullets.remove(game_object)
        if game_object.type == "enemy":
            self.enemies.remove(game_object)
    
    def check_hit(self):
        for enemy in game_manager.enemies:
            for bullet in game_manager.bullets :
                if bullet.y < 0 or bullet.y>800:
                    game_manager.remove(bullet)
                elif bullet.x >= enemy.x - enemy.image.get_width() and bullet.x<= enemy.x + enemy.image.get_width()\
                        and bullet.y <= enemy.y + enemy.image.get_height()/2:
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