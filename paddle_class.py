from turtle import Turtle

INCREMENT = 20
STRETCH_WID = 5
STRETCH_LEN = 1
PADDLE_COLOR = "white"

class Paddle(Turtle):
    def __init__(self, x_axis):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=STRETCH_WID,stretch_len=STRETCH_LEN)
        self.color(PADDLE_COLOR)
        self.teleport(x=x_axis, y=0)
        self.penup()

    def up(self):
        if self.ycor() < 260:
            self.goto(x=self.xcor(), y=self.ycor() + INCREMENT)

    def down(self):
        if self.ycor() > -260:
            self.goto(x=self.xcor(), y=self.ycor() - INCREMENT)
