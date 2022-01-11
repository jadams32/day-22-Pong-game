from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ('Chalkboard', 28, 'normal')


class Scoreboard(Turtle):

    def __init__(self, x_loc, y_loc, side):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x_loc, y_loc)
        self.draw_scoreboard(side)
        self.draw_scoreboard(side)

    def draw_scoreboard(self, side):
        if side == "left":
            score = self.left_score
        elif side == "right":
            score = self.right_score

        self.write(f"Score: {score}", move=False, align=ALIGNMENT, font=FONT_STYLE)

    def update_left_scoreboard(self):
        self.left_score += 1
        self.clear()
        self.draw_scoreboard("left")

    def update_right_scoreboard(self):
        self.right_score += 1
        self.clear()
        self.draw_scoreboard("right")


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
