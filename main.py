# TODO: create scoreboard class
# TODO: create pong ball class
# TODO: create paddle class
# TODO: update the scoreboard when a player scores
# TODO: reset the pong ball if the players miss the ball
# TODO: Create game play field using screen and turtles

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Net
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Classic Pong")
screen.bgcolor("black")
screen.tracer(0)

net = Net()
net.draw_net()
left_scoreboard = Scoreboard()
left_scoreboard.draw_left_scoreboard()
right_scoreboard = Scoreboard()
right_scoreboard.draw_right_scoreboard()

screen.update()
right_paddle = Paddle()
right_paddle.draw_right_paddle()

left_paddle = Paddle()
left_paddle.draw_left_paddle()

screen.update()

screen.exitonclick()
