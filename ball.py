from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10
        self.move_speed = .07

    def move(self):
        """Starts movement for the pong ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        return new_y, new_x

    def change_direction_y(self):
        """Changes the ball's direction."""
        self.y_move *= -1

    def change_direction_x(self):
        """Changes the ball's direction."""
        self.x_move *= -1
        self.move_speed *= .8

    def reset_ball(self):
        """Resets the ball to the center of the screen."""
        self.goto(0, 0)

    def reset_speed(self):
        """Resets the speed of the ball, to standard."""
        self.move_speed = .1
