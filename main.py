# TODO: create scoreboard class
# TODO: create pong ball class
# TODO: create paddle class
# TODO: update the scoreboard when a player scores
# TODO: reset the pong ball if the players miss the ball
# TODO: Create game play field using screen and turtles

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


net = Turtle()
net.hideturtle()
net.color("white")
net.pencolor("white")
net.pensize(5)
net.setheading(90)
net.hideturtle()
net.penup()
net.goto(x=0, y=-600)
net.pendown()


for num in range(60):
    net.forward(10)
    net.penup()
    net.forward(10)
    net.pendown()






screen.exitonclick()
