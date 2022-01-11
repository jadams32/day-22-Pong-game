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
screen.title("Classic Pong")
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


screen.update()
right_paddle = Turtle("square")
right_paddle.color("White")
right_paddle.setheading(90)
right_paddle.turtlesize(stretch_wid=None, stretch_len=5)
right_paddle.penup()
right_paddle.goto(x=350, y=0)

left_paddle = Turtle("square")
left_paddle.color("White")
left_paddle.setheading(90)
left_paddle.turtlesize(stretch_wid=None, stretch_len=5)
left_paddle.penup()
left_paddle.goto(x=-350, y=0)
screen.update()

screen.exitonclick()
