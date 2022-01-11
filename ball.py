from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.y_move = 2
        self.x_move = 2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def change_direction_y(self):
        self.y_move *= -1

    def change_direction_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
