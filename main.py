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
left_scoreboard = Scoreboard(-200, 260, "left")
right_scoreboard = Scoreboard(200, 260, "right")

screen.update()
right_paddle = Paddle(380, 0)
left_paddle = Paddle(-380, 0)

ball = Ball()

screen.update()

screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")
screen.update()

playing = True

while playing:
    screen.update()
    ball.move()

screen.exitonclick()
