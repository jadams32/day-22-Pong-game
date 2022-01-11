from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + 2
        new_y = self.ycor() + 2
        self.goto(new_x, new_y)

    def change_direction(self):
        new_x = self.xcor() + 2
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0, 0)
