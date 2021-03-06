from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_loc, y_loc):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_wid=None, stretch_len=5)
        self.penup()
        self.goto(x_loc, y_loc)

    def up(self):
        """Moves the paddle up."""
        self.forward(30)

    def down(self):
        """Moves the paddle down."""
        self.back(30)
