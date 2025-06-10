import turtle
from random import randint 
import time

t= turtle.Turtle()
t.speed(0) # Set to 0 for fastest drawing speed
t.ht()
t.fillcolor("white")
t.pensize(5)

def blades(t, deg, radius, x, y):
    # Move the pen to the position
    t.penup()
    t.setpos(x,y)
    # Change deg so the blades will be drawn at a different angle
    t.seth(deg)
    t.pendown()

    # Fill with white colours
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

    # Drawing the 3rd blade
    t.seth(deg+240)
    t.circle(radius, 30)  
    t.left(150)
    t.circle(radius, 30)  
    
    t.end_fill()

blades(t, 0, 150, 0, 0)
turtle.done()