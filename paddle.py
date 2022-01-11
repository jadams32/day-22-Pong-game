from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")

    def draw_right_paddle(self):
        self.setheading(90)
        self.turtlesize(stretch_wid=None, stretch_len=5)
        self.penup()
        self.goto(x=350, y=0)

    def draw_left_paddle(self):
        self.setheading(90)
        self.turtlesize(stretch_wid=None, stretch_len=5)
        self.penup()
        self.goto(x=-350, y=0)
