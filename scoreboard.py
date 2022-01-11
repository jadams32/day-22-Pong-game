from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ('Chalkboard', 28, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")

    def draw_left_scoreboard(self):
        self.goto(-200, 260)
        self.write(f"Score: {self.left_score}", move=False, align=ALIGNMENT, font=FONT_STYLE)

    def draw_right_scoreboard(self):
        self.goto(200, 260)
        self.write(f"Score: {self.right_score}", move=False, align=ALIGNMENT, font=FONT_STYLE)

    def update_left_scoreboard(self):
        self.left_score += 1
        self.clear()
        self.draw_left_scoreboard()

    def update_right_scoreboard(self):
        self.right_score += 1
        self.clear()
        self.draw_left_scoreboard()


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
