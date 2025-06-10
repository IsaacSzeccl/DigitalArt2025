import turtle
from random import randint 
import time

sc = turtle.Screen()
sc.setup(500, 500) 
sc.tracer(0) # to update each frame manually after drawing by sc.update()

def build_turtle(speed, pensize, color=None, fillcolor=None):
    t= turtle.Turtle()
    t.speed(speed) # Set to 0 for fastest drawing speed
    t.ht()
    t.pensize(pensize)
    if color: t.color(color)
    if fillcolor: t.fillcolor(fillcolor)
    return t

wind1 = build_turtle(0, 5, "blue", None)
wind2 = build_turtle(0, 5, "blue", None)

frame = 0
wind_pos = -300 # the wind will be generated at x=-200, -100, 0, 100

def wind(t, x, y):
    t.penup()
    t.setpos(x,y)
    t.seth(0)
    t.pendown()
    t.fd(30) # Length of the wind tail
    t.circle(8, 270) # Size of the circle after the wind tail

while True:
    if frame%3 == 0: 
        wind1.clear()
        wind2.clear()
        wind(wind1, wind_pos, 0)
        wind(wind2, wind_pos+100, -20)
        wind_pos += 100
        if wind_pos > 200:
            # reset wind_pos once out of range
            wind_pos = -300
    time.sleep(0.1)
    frame += 1
    sc.update()