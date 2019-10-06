import pgzrun
import pgzero
from random import randint

def resetpos():
    boy.x=595
    boy.y=630

WIDTH=1200
HEIGHT=850
TITLE='Game 2'
monster_hp=100
game_over=False

monster=Actor('monster')
monster.pos=randint(0,1200),randint(0,850)
boy=Actor('boy')
boy.pos=595,630

def draw():
    global monster_hp, game_over
    screen.clear()
    screen.blit('bg1',(0,0))
    boy.draw()
    screen.draw.text(str(monster_hp),color='white',topleft=(0,0))
    if game_over:
        screen.draw.textbox('GAME OVER',Rect(350,50,500,700),color='white')

def update():
    speed=1
    if keyboard.RIGHT:
        boy.x+=speed
        if boy.x>WIDTH:
            resetpos()
    if keyboard.LEFT:
        boy.x-=speed
        if boy.x<0:
            resetpos()
    if keyboard.DOWN:
        boy.y+=speed
        if boy.y>HEIGHT:
            resetpos()
    if keyboard.UP:
        boy.y-=speed
        if boy.y<0:
            resetpos()

def on_key_down(key):
    global monster_hp, game_over
    if key==keys.SPACE:
        if boy.colliderect(monster):
            monster_hp-=10
            if monster_hp<1:
                monster.image='stones'
                game_over=True

pgzrun.go()