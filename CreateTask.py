import turtle
import time
#variables
x = 0
g = 9.8
seconds = 1
wn = turtle.Screen()
wn.bgcolor('lightblue')
d =  1
#turtles
character = turtle.Turtle()
character.color('brown')
character.penup()
character.speed(0)
character.dy = -2
def left():
    character.setheading(0)
def right():
    character.setheading(180)
def press_seconds():
    global seconds
    seconds = time.time()
    wn.onkeypress(None, ' ')
def release_seconds():
    if seconds >= 3:
        wn.onkeyrelease(None, ' ')
    global d
    d *= seconds
def jump():
    character.fd(d)

while True:
    wn.update()
    if character.ycor() > -276:
        character.sety(character.ycor() + character.dy)
    else:
        pass
    wn.listen()
    wn.onkey(left, "d")
    wn.onkey(right, "a")
character.onkeyrelease()

turtle.mainloop()
