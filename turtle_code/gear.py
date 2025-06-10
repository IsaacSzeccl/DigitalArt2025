import turtle
from random import randint 
import time

sc = turtle.Screen()  
sc.setup(500, 500) 
sc.tracer(0)
# sc.bgpic("python-drawing/turtle_code/mountain.png")


def build_turtle():
    t= turtle.Turtle()
    t.speed(5)
    t.ht()
    t.pensize(5)
    t.color("blue")
    return t

def draw_gear(t, deg, radius, teeth, teeth_size, x, y):
    t.penup()
    t.goto(x,y-radius)
    t.pendown()
    t.circle(radius)

    for tooth_index in range(teeth):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.seth(360//teeth*tooth_index+deg)
        t.penup()
        t.forward(radius+teeth_size)
        t.pendown()

        t.right(90)
        t.forward(teeth_size)
        t.right(80)
        t.forward(teeth_size)
        t.right(180)
        t.forward(teeth_size)
        t.left(80)
        t.forward(teeth_size*2)
        t.left(80)
        t.forward(teeth_size)
    t.penup()
    t.seth(0)
    t.goto(x,y-radius//3)
    t.pendown()
    t.circle(radius//3)

t1 = build_turtle()
t2 = build_turtle()
t3 = build_turtle()

frame = 0 

while True:
    time.sleep(0.01) # decide delay between each frame
    draw_gear(t1, frame, 50, 8, 10, 0, 0)
    draw_gear(t2, -frame+20, 50, 8, 10, -82, -80)
    draw_gear(t3, -frame+20, 50, 8, 10, 78, -80)
    sc.update()
    t1.clear()
    t2.clear()
    t3.clear()
    frame += 1

