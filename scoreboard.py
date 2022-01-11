from turtle import Turtle


class Scoreboard(Turtle):
    pass


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pencolor("white")
        self.pensize(5)
        self.setheading(90)

    def draw_net(self):
        self.penup()
        self.goto(x=0, y=-600)
        self.pendown()
        for num in range(60):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()