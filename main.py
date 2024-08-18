from turtle import Screen, Turtle
from paddle_class import Paddle

BG_COLOR = "black"
WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(350)
paddle_left = Paddle(-350)

ball = Turtle(shape="circle")
ball.color("white")
ball.goto(x=380, y=280)


screen.listen()
screen.onkey(fun=paddle_right.up, key="Up")
screen.onkey(fun=paddle_right.down, key="Down")
screen.onkey(fun=paddle_left.up, key="w")
screen.onkey(fun=paddle_left.down, key="s")


game_is_on = True
while game_is_on:
    screen.update()














screen.exitonclick()
