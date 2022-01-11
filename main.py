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
    # Detect Collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction_y()

    # Detect if left user scores a point
    if ball.xcor() > 400:
        left_scoreboard.update_left_scoreboard()
        ball.reset_ball()

    # Detect if right user scores a point
    if ball.xcor() < -400:
        right_scoreboard.update_right_scoreboard()
        ball.reset_ball()

    # Detect collision with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 360:
        ball.change_direction_x()

    # Detect collision with the left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.change_direction_x()


screen.exitonclick()
