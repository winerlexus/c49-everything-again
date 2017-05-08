
##generate matrix:
def display_map(size,pusher,boxlist,potal):
    for y in range(0,size['y']+2):
        for x in range(0,size['x']+2):
            #content_map
            if x==pusher['x'] and y==pusher['y']:
                print(' p ',end='')
            #boxes:
            elif x==box['x'] and y==box['y']:
                    print(' b ',end='')
            elif x==potal['x'] and y==potal['y']:
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
    if move=="A":
        pusher['x']-=1
        move_modify(pusher['x'])
    elif move=='D':
        pusher['x']+=1
        move_modify(pusher['x'])
    elif move=='W':
        pusher['y']-=1
        move_modify(pusher['y'])
    elif move=='S':
        pusher['y']+=1
        move_modify(pusher['y'])
    box_move()
        
def box_move():
    #horizontal move
    if pusher['y']==box['y']:
        if pusher['x'] ==box['x']:
            if move=='D':
                box['x']=box['x']+1
                if box['x']==bdx[1]:
                    box['x']-=1
                    pusher['x']-=1
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

## prevent box or player movement from obstacle
def move_modify(a):
    #horizontal border:
    if move=='A':
        if a==bdx[0]:
            a+=1
    elif move=='D':
        b='x'
        if a==bdx[1]:
            a-=1  
    #vertical border:
    if move=='S':
        b='y'
        if a==bdx[1]:
            a-=1
    elif move=='W':
        b='y'
        if a==bdx[0]:
            a+=1

size={
    'x':5,
    'y':5
    }
pusher={
    'x':1,
    'y':1
    }
box={
    'x':3,
    'y':3
    }
box2={
    'x':10,
    'y':6
    }
potal={
    'x':3,
    'y':5
    }
potal2={
    'x':1,
    'y':5
    }
boxlist=[box,box2]
print(boxlist)
#Game loop
if box['x']==potal['x'] and box['y']==potal['y']:
    loop=False
else:
    loop=True
move=0
bdx=[0,size['x']+1]
bdy=[0,size['y']+1] 
while(loop):
    display_map(size,pusher,box,potal)
    move=input('your move?').upper()
    pusher_move()
    print(box)
    print(potal)


