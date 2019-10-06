import pgzrun
import pgzero
from random import randint

WIDTH=1000
HEIGHT=700
TITLE='Mushroom Bonanza'
mushrooms=[]
mushroomnum=6
score=0
counter=0

def reset_image():
    for g in range(6):
        if not mushrooms[g].image=='bomb':
            mushrooms[g].image='mushroom0'

for i in range(mushroomnum):
    mushrooms.append(Actor('mushroom0'))
    mushrooms[i].pos=randint(0,1000),randint(375,600)

def draw():
    global score
    screen.clear()
    screen.blit('grass',(0,0))
    for j in range(mushroomnum):
        mushrooms[j].draw()
    screen.draw.text('SCORE : '+str(score),topleft=(10,10),color='black')

def update():
    global counter
    if counter>4:
        for e in range(6):
            if randint(0,1)==0:
                mushrooms[e].x+=randint(10,20)
                if mushrooms[e].x>1000:
                    mushrooms[e].pos=randint(0,1000),randint(375,600)
            else:
                mushrooms[e].x-=randint(10,20)
                if mushrooms[e].x<0:
                    mushrooms[e].pos=randint(0,1000),randint(375,600)
        counter=0
    else:
        counter+=1

def on_mouse_down(pos):
    global score
    for x in range(6):
        if mushrooms[x].collidepoint(pos):
            if mushrooms[x].image=='bomb':
                score-=2
                mushrooms[x].image='explotion'
            else:
                rnum=randint(1,5)
                if rnum==2:
                    mushrooms[x].image='bomb'
                else:
                    mushrooms[x].image='mushroom'+str(rnum)
                    clock.schedule_unique(reset_image,0.3)
                    score+=1

pgzrun.go()