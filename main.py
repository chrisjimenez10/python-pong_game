from turtle import Screen
from paddle_class import Paddle

BG_COLOR = "black"
WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title("Pong")
screen.tracer(0)

paddle_one = Paddle()
paddle_one.set_position(350)
paddle_two = Paddle()
paddle_two.set_position(-350)

screen.listen()
screen.onkey(fun=paddle_one.up, key="Up")
screen.onkey(fun=paddle_one.down, key="Down")
screen.onkey(fun=paddle_two.up, key="w")
screen.onkey(fun=paddle_two.down, key="s")


game_is_on = True
while game_is_on:
    screen.update()














screen.exitonclick()
