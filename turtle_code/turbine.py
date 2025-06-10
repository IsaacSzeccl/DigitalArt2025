import turtle
from random import randint 
import time

def build_turtle(speed, pensize, color=None, fillcolor=None):
    t= turtle.Turtle()
    t.speed(speed) # Set to 0 for fastest drawing speed
    t.ht()
    t.pensize(pensize)
    if color: t.color(color)
    if fillcolor: t.fillcolor(fillcolor)
    return t

# Create turtles
t1 = build_turtle(0, 5, "black", "white")
circle_turtle = build_turtle(0, 5, "black", "white")
base_turtle = build_turtle(0, 5, "black", "white")
wind1 = build_turtle(0, 5, "blue", None)
wind2 = build_turtle(0, 5, "blue", None)

sc = turtle.Screen()  
sc.setup(1024, 1024) 
sc.tracer(0) # to update each frame manually after drawing by sc.update()
# sc.bgpic("python-drawing/turtle_code/mountain.png")

def draw_circle(t, radius, x, y):
    # Draw a filled circle for the center of wind turbine
    t.begin_fill() 
    t.penup()
    t.goto(x, y-radius) 
    t.seth(0)
    t.pendown()  
    t.circle(radius)  
    t.end_fill()

def draw_base(t, x, y, w, h):
    # Draw the base of the wind turbine
    t.penup()
    t.setpos(x,y)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.fd(w//2)
    t.right(90)
    t.fd(h)
    t.right(90)
    t.fd(w)
    t.right(90)
    t.fd(h)
    t.right(90)
    t.fd(w//2)
    t.end_fill()

def blades(t, deg, radius, x, y):
    t.penup()
    t.setpos(x,y)
    t.seth(deg)
    t.pendown()

    t.begin_fill()
    # Drawing the 1st blade
    t.circle(radius, 30)  
    t.left(150)
    t.circle(radius, 30)  

    # Drawing the 2nd blade
    t.seth(deg+120)
    t.circle(radius, 30)  
    t.left(150)
    t.circle(radius, 30)   

    t.seth(deg+240)
    t.circle(radius, 30)  
    t.left(150)
    t.circle(radius, 30)  
    t.end_fill()

def draw_turbine(x, y, deg):
    draw_base(base_turtle, x, y, 10, 100) 
    blades(t1, deg, 100, x, y)
    draw_circle(circle_turtle, 10, x, y)

wind_pos = -400 # the wind will be generated at x=-200, -100, 0, 100
frame = 0 

while True:
    time.sleep(0.01) # decide delay between each frame
    
    draw_turbine(0, 0, frame*3)
    
    sc.update()

    t1.clear()
    frame += 1