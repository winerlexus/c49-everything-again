# -*- coding: utf-8 -
import pygame
import random
pygame.init()
pygame.display.set_caption("La Hán Đẩy Xe BÒ")
screen = pygame.display.set_mode((1080,1024))

mario_image = pygame.image.load("sprites/mario.png")
brick_image = pygame.image.load("sprites/square.png")
box_image = pygame.image.load("sprites/box.png")
mario={}
box={}
brick_width=brick_image.get_width()
brick_height=brick_image.get_height()

col_count = 5
row_count = 5

clock = pygame.time.Clock()
#mario info
mario_x = 0
mario_y = 0

mario_col = 0
mario_row = 0

mario_next_col=0
mario_next_row=0

box_next_col=0
box_next_row=0
#box info
box_col = random.randrange(1,col_count)
box_row = random.randrange(1,col_count)

box_width = box_image.get_width()
box_height = box_image.get_height()


time=0



def in_map(object_next_col, object_next_row):
    if object_next_col >= 0 and object_next_col < col_count \
        and object_next_row >= 0 and object_next_row < row_count:
            return True
   
    return False

loop = True   
while loop:
    dx=0
    dy=0 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
#                    right_press = True
                dx = 1 
            elif event.key == pygame.K_LEFT:
                print("LEFT")
#                    left_press = True
                dx = -1
            elif event.key == pygame.K_UP:
                print("UP")
#                    up_press = True
                dy = -1
            elif event.key == pygame.K_DOWN:
                print("DOWN")
#                    down_press = True
                dy = 1
            else: 
                pass

            mario_next_col = mario_col + dx
            mario_next_row = mario_row + dy
            
            if in_map(mario_next_col, mario_next_row):
                print('curent mario',mario_col,mario_row)
                print('future mario',mario_next_col,mario_next_col)
                print('curent box',box_col, box_row)
                if (mario_next_col,mario_next_row) == (box_col, box_row):
                    box_next_col = box_col + dx
                    box_next_row = box_row + dy
                    if in_map(box_next_col,box_next_row):
                        mario_col = mario_next_col
                        mario_row = mario_next_row
                        box_col = box_next_col
                        box_row = box_next_row
                elif (mario_next_col,mario_next_row) != (box_col, box_row):
                    mario_col = mario_next_col
                    mario_row = mario_next_row        
            
            
           
#        elif event.type == pygame.KEYUP:
#                if event.key == pygame.K_RIGHT:
#                    right_press = False
#                elif event.key == pygame.K_LEFT: 
#                    left_press = False
#                elif event.key == pygame.K_UP:
#                    up_press = False
#                elif event.key == pygame.K_DOWN:
#                    down_press = False
#    time += 1
#    if time >=7.5:
#        time = 0
               
#        if right_press:
#            mario_row+=1
#        elif left_press:
#            mario_row-=1
#        elif up_press:
#            mario_col-=1
#        elif down_press:
#            mario_col+=1             
    screen.fill((255,255,255))
    # display bricks
    for row in range(0,row_count):
        for col in range(0,col_count):
            x = col * brick_width
            y = row * brick_height
            screen.blit(brick_image,(x,y))
   
    #display mario         
    mario_x = mario_col * brick_width
    mario_y = mario_row * brick_height
       
    screen.blit(mario_image,(mario_x , mario_y))
    
    #display box
    box_x = box_col * box_width
    box_y = box_row * box_height
    screen.blit(box_image,(box_x , box_y ))
    clock.tick(60)
    pygame.display.flip()
    

pygame.quit()
