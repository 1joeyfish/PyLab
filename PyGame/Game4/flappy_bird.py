import pgzrun
import pgzero
from random import randint

WIDTH=800
HEIGHT=708
TITLE='Flappy bird'
gap=150
speed=2
speedy=1

def reset_pipes():
    global gap
    bottom.pos=WIDTH-100,randint(200,500)
    top.pos=WIDTH-100,bottom.y-gap

def change():
    if bird.image=='bird0':
        bird.image='bird1'
    if bird.image=='bird1':
        bird.image='bird2'
    if bird.image=='bird2':
        bird.image='bird0'

bottom=Actor('bottom',anchor=('left','top'))
top=Actor('top',anchor=('left','bottom'))
bird=Actor('bird0')
bird.pos=100,HEIGHT/2
reset_pipes()

def draw():
    screen.clear()
    screen.blit('background',(0,0))
    bottom.draw()
    top.draw()
    bird.draw()

def update_pipes():
    bottom.x-=speed
    top.x-=speed
    if bottom.x<1:
        reset_pipes()

def update_bird():
    global speedy
    bird.y+=speedy
    speedy+=0.02

def update():
    global speedy
    update_pipes()
    update_bird()
    clock.schedule_unique(change,0.3)
    if keyboard.SPACE:
        speedy=0
        bird.y-=5
    if bottom.colliderect(bird) or top.colliderect(bird):
        bird.image='birddead'


pgzrun.go()