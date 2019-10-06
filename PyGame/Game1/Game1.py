import pgzrun
import pgzero

def resetpos():
    global speed
    alien.x=WIDTH/2
    alien.y=HEIGHT/2
    alien.angle=0
    speed=0

speed=2
WIDTH=1000
HEIGHT=750
TITLE='Game 1'

alien=Actor('alien')
alien.pos=WIDTH/2,HEIGHT/2
alien.angle=0

def draw():
    say='SPEED : '+str(speed)
    screen.clear()
    screen.fill('light sky blue')
    alien.draw()
    screen.draw.text(say,color='black',topleft=(0,0))
    screen.draw.text('ANGLE : '+str(alien.angle),color='black',topleft=(0,20))


def update():
    global speed, say

    if keyboard.right:
        alien.x+=speed
        if alien.x>WIDTH:
            resetpos()
    if keyboard.left:
        alien.x-=speed
        if alien.x<0:
            resetpos()
    if keyboard.down:
        alien.y+=speed
        if alien.y>HEIGHT:
            resetpos()
    if keyboard.up:
        alien.y-=speed
        if alien.y<0:
            resetpos()

def on_mouse_down(button):
    global speed
    if button==mouse.WHEEL_UP:
        speed+=1
    if button==mouse.WHEEL_DOWN:
        speed-=1
    if button==mouse.LEFT:
        if alien.image=='alien':
            alien.image='alien_hurt'
        elif alien.image=='alien_hurt':
            alien.image='alien'

def on_key_down(key):
    global speed
    if key==keys.E:
        alien.angle+=speed
    if key==keys.T:
        alien.angle-=speed
    if key==keys.R:
        resetpos()

pgzrun.go()