# Import library code
from p5 import *
from random import randint

# The mouse_pressed function goes here
def mouse_pressed():
    #print('🎯')
    if hit_colour == Color('blue').hex:
        print('You hit the outer circle, 50 points!')
    elif hit_colour == Color('red').hex:
        print('You hit the inner circle, 200 points!')
    elif hit_colour == Color('yellow').hex:
        print('You hit the middle, 500 points!')
    else:
        print('You missed! No points!')
# The shoot_arrow function goes here
def shoot_arrow():
    global hit_colour
    arrow_x = randint(100, 300)
    arrow_y = randint(100, 300)
    hit_colour = get(arrow_x, arrow_y).hex
    #print(hit_colour)
    fill('sienna')
    circle(arrow_x, arrow_y, 15)


def setup():
    # Setup your game here
    size(400, 400)


def draw():
    # Things to do in every frame
    fill('cyan')
    rect(0, 0, 400, 250)
    fill('lightgreen')
    rect(0, 250, 400, 150)
    fill('sienna')
    triangle(150, 350, 200,150,250, 350)
    fill('blue')
    circle(200, 200, 170)
    fill('red')
    circle(200, 200, 110)
    fill('yellow')
    circle(200, 200, 30)
    shoot_arrow()
    
# Keep this to run your code
run(frame_rate=2)
