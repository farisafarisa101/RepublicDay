import turtle
from turtle import *
from pygame import mixer
# Code for Music
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()

screen =turtle.Screen()
turtle.hideturtle()

screensize(100,1000)
bgpic('india.gif')
t=turtle.Turtle()
speed(0)
t.penup()
t.goto(-350,350)
t.pendown()
#Orange color
t.color("Orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(80)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(80)

#Green color
t.color("Green")
t.begin_fill()
t.forward(80)
t.left(90)
t.forward(400)
t.left(90)
t.forward(80)
t.end_fill()

#Blue circle
t.penup()
t.goto(-105,230)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(40)
t.end_fill()

#White circle
t.penup()
t.goto(-111,230)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(34)
t.end_fill()

#spokes
t.penup()
t.goto(-145,230)
t.pendown()
t.color("navy")
t.pensize(2)
for i in range(24):
    t.backward(34)
    t.forward(34)
    t.left(15)
#pole
t.penup()
t.goto(-350,350)
t.pendown()
t.color("gray")
t.fillcolor()
t.pensize(15)
t.backward(500)

#pole size
def rectangle():
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)

rectangle()
t.right(90)
t.forward(40)
rectangle()
t.forward(120)
rectangle()
t.right(90)
t.forward(40)
t.left(90)
t.forward(40)

text =turtle.Turtle()
text.hideturtle()
text.speed(1)

def write(message,pos,color):
    x,y=pos
    text.color(color)
    text.penup()
    text.goto(x,y)
    text.pendown()
    style=('Arial',40,'italic')
    text.write(message,font=style)
write('Happy',(200,-70),'orange')
write('Republic',(250,-130),'blue')
write('Day' ,(200,-190),'green')
t.penup()
t.goto(50,-240)
t.color('black')
t.write('-Farisa Fatema',align='left',
        font=('Courier',20,'bold'))
t.fillcolor('black')
t.hideturtle()
turtle.mainloop()
