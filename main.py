# TODO: Add a life system to where each player has three lives

# Imports from other files needed to run the game.
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Net, Winner
import time

# Screen initialization and title, background color, animation, and size set up.
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Classic Pong")
screen.bgcolor("black")
screen.tracer(0)


# Initializing the net in the middle of the screen.
net = Net()
net.draw_net()

# Initializing the players scoreboards
left_scoreboard = Scoreboard(-200, 260, "left")
right_scoreboard = Scoreboard(200, 260, "right")

# Initializing the left and right players paddles
right_paddle = Paddle(380, 0)
left_paddle = Paddle(-380, 0)

# Initializing the pong ball.
ball = Ball()

# Initializing the winner.
winner = Winner()

# Since animations have been turned off we need to update the screen with this command to show the previous initialized
# items on screen.
screen.update()

# This tells the screen to listen for any inputs from the users
screen.listen()

# The right players inputs for up and down, "up arrow" moves the paddle up and "down arrow" moves the paddle down
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
# The left players inputs for up and down, "W" moves the paddle up and "S" moves the paddle down
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")
screen.update()

# While loop variable to determine when to stop the game.
playing = True

while playing:
    # Update the animations on the screen according to if the ball has hit a users paddle. This speeds up the ball,to
    # make the game harder over time
    screen.update()
    time.sleep(ball.move_speed)

    # Start the pong ball movement
    ball.move()

    # Detect Collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction_y()

    # Detect if left user scores a point
    if ball.xcor() > 400:
        left_scoreboard.update_left_scoreboard()
        ball.reset_ball()
        ball.reset_speed()
        ball.change_direction_x()

    # Detect if right user scores a point
    if ball.xcor() < -400:
        right_scoreboard.update_right_scoreboard()
        ball.reset_ball()
        ball.reset_speed()
        ball.change_direction_x()

    # Detect collision with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 360:
        ball.change_direction_x()

    # Detect collision with the left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.change_direction_x()

    # If the left user earns 10 points, stop the game and display winner.
    if left_scoreboard.left_score == 10:
        winner.who_won("left")
        playing = False

    # If the right user earns 10 points, stop the game and display winner.
    if right_scoreboard.right_score == 10:
        winner.who_won("right")
        playing = False

# When the user clicks the screen closes and ends the program.
screen.exitonclick()
