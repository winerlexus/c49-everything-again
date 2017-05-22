####[]not complete for overall cases
####[]not solve cases which are 2 box next to each other
####[]''game loop'' is not completed 
##generate matrix:
def display_map(size,pusher,box,potal):
    for y in range(0,size['y']+2):
        for x in range(0,size['x']+2):
            #content_map
            if x==pusher['x'] and y==pusher['y']:
                print(' p ',end='')
            #boxes:
            elif x==box1['x'] and y==box1['y']:
                    print(' b ',end='')
            elif x==box2['x'] and y==box2['y']:
                print(' b ',end='')
            elif x==potal1['x'] and y==potal1['y']:
                print(' g ',end='')
            elif x==potal2['x'] and y==potal2['y']:
                print(' g ',end='')
            #border:
            elif x==0:
                print(' w ',end='')
            elif x==size['x']+1:
                print(' w ',end='')
            elif y==0:
                print(' w ',end='')
            elif y==size['y']+1:
                print(' w ',end='')
            else:
                print(' - ',end='')
        print('')

def pusher_move():
    if move=="A" and pusher['x']>1:
        pusher['x']-=1
##        if pusher['x']==bdx[0]:
##            pusher['x']+=1
    elif move=='D' and pusher['x']<size['x']:
        pusher['x']+=1
##        if pusher['x']==bdx[1]:
##             pusher['x']-=1
    elif move=='W' and pusher['y']>1:
        pusher['y']-=1
##        if pusher['y']==bdx[0]:
##            pusher['y']+=1
    elif move=='S' and pusher['y']<size['y']:
        pusher['y']+=1
##        if pusher['y']==bdx[0]:
##            pusher['y']+=1
    for i in boxlist:
        box_move(i)
        
def box_move(box):
    #horizontal move
    if pusher['y']==box['y'] and pusher['x'] ==box['x']:
            if move=='D' and box['x']<size['x'] and pusher['x']<size['x']-1:
                box['x']=box['x']+1
##                if box['x']==size['x']-1:
##                    box['x']-=1
##                    pusher['x']-=1
            elif move=='A':
                box['x']=box['x']-1
                if box['x']==bdx[0]:
                    box['x']+=1
                    pusher['x']+=1
    #vertical move
    if pusher['x']==box['x']:
        if pusher['y']==box['y']:
            if move=='W':
                box['y']=box['y']-1
                if box['y']==bdy[0]:
                    box['y']+=1
                    pusher['y']+=1 
                    
            elif move=='S':
                box['y']=box['y']+1
                if box['y']==bdy[1]:
                    box['y']-=1
                    pusher['y']-=1
def in_map(size,point):
    return point['x']>=0 and point['x']<size['x'] \
           and point['y']>=0 and point['y']<size['y']
size={
    'x':5,
    'y':5
    }
pusher={
    'x':1,
    'y':1
    }
box1={
    'x':3,
    'y':3
    }
box2={
    'x':4,
    'y':5
    }
potal1={
    'x':3,
    'y':5
    }
potal2={
    'x':1,
    'y':5
    }
boxlist=[box1,box2]
potallist=[potal1,potal2]
#Game loop
if box1['x']==potal1['x'] and box1['y']==potal1['y']:
    loop=False
else:
    loop=True
move=0
bdx=[0,size['x']+1]
bdy=[0,size['y']+1] 
while(loop):
    ##graphics
    display_map(size,pusher,box1,potal1)
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

    pusher_next={}
    pusher_next['x']=pusher['x']+dx
    pusher_next['y']=pusher['y']+dy
    if in_map(size,pusher):
        pusher=pusher_next
        
    pusher_move()
    print(pusher['x'])
