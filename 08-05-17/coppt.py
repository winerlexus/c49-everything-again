import random
def position_in_list(positions,x,y):
    for box in positions:
        if box['x']==x and box['y']==y:
            return positions.index(box)
    return None

def display_map(size,pusher,box_list,potal_list):
    for y in range(1,size['y']+1):
        for x in range(1,size['x']+1):
            #content_map
            if x==pusher['x'] and y==pusher['y']:
                print('p',end='')
            #boxes:
            elif position_in_list(box_list,x,y) is not None:
                print('b',end='')
            #potals
            elif position_in_list(potal_list,x,y)is not None:
                print('g',end='')
            elif position_in_list(obs_list,x,y) is not None:
                print('o', end='')
            else:
                print('-',end='')
        print('')
def in_map(size,point):
    return point['x']>=0 and point['x'] < size['x']+1\
           and point['y']>=0 and point['y'] < size['y']+1

def same_point(point1,point2):
            return point1['x']==point2['x'] and point1['y']==point2['y']
        
def move_point(point,dx,dy):
    return  {
            'x' : point['x']+dx,
            'y' : point['y']+dy
            }
size={
        'x':5,
        'y':5
    }
pusher={
        'x':1,
        'y':1
    }
potal_list=[
    {
        'x':3,
        'y':5
    },
    {
        'x':1,
        'y':5
    }
    ]
obs_list=[
    {
        'x':4,
        'y':3
    },
    {
        'x':2,
        'y':2
    }
        ]
box_list=[
    {
        'x':3,
        'y':3
    },
    {
        'x':4,
        'y':5
    }
    ]
bonus_x=random.randrange(1,size['x']+1)
bonus_y=random.randrange(1,size['y']+1)

print('bonus_x {0}, bonus_y {1}'.format(bonus_x,bonus_y))
rand_index=len(box_list)-1
loop=True
while(loop):
    ##graphics
    display_map(size,pusher,box_list,potal_list)
    ##gameplay
    move=input('your move?').upper()
    dx=0
    dy=0
    if move=='D':
        dx=1
    elif move=='A':
        dx=-1
    elif move=='W':
        dy=-1
    elif move=='S':
        dy=1

    pusher_next= move_point(pusher,dx,dy)
    if in_map(size,pusher_next):
        #move allowed, check boxes front:?
        box_index=position_in_list(box_list,pusher_next['x'],pusher_next['y'])
        if box_index is not None:
            #Box front, try to fuk it
            box_next=move_point(box_list[box_index],dx,dy)
##            print(box_next)
            if in_map(size,box_next):
                otherbox_index=position_in_list(box_list,box_next['x'],box_next['y'])
                obs_index=position_in_list(obs_list,box_next['x'],box_next['y'])
                potal_index=position_in_list(potal_list,box_next['x'],box_next['y'])
##                print(otherbox_index)
                if (obs_index is None) and (otherbox_index is None):
                # good to go no boxes or obs ahead
                    box_list[box_index]=box_next
                    pusher=pusher_next
                    if potal_index is not None:
                    #potal ahead
##                        print(potal_index)
                        box_list.remove(box_list[box_index])
                        potal_list.remove(potal_list[potal_index])
##                        print(box_list)
##                        print(potal_list)
                else:
                    box_next=box_list[box_index]
                    
        elif position_in_list(obs_list,pusher_next['x'],pusher_next['y']) is not None:
            #blocked
            pusher_next=pusher
        elif pusher_next['x']==bonus_x and pusher_next['y']==bonus_y:
            #random remove 1 box and 1 gate/ bonus
            box_list.remove(box_list[random.randrange(rand_index)])
            potal_list.remove(potal_list[random.randrange(rand_index)])
            pusher=pusher_next
            bonus_x=0
            bonux_y=0
            print(bonus_x)
            print(bonus_y)
        elif box_list==[]:
            print('You fkin made it')
            loop=False
        else:
            #nothing ahead
            pusher=pusher_next
