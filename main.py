from turtle import Screen, Turtle
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import ScoreBoard
import time

BG_COLOR = "black"
WIDTH = 800
HEIGHT = 600

screen = Screen()

left_player = screen.textinput(title="Left Player:", prompt="What is your name?:")
if not left_player:
    left_player = "Left Player"
right_player = screen.textinput(title="Right Player:", prompt="What is your name?:")
if not right_player:
    right_player = "Right Player"

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(350)
paddle_left = Paddle(-350)
ball = Ball()
score = ScoreBoard(left_player=left_player, right_player=right_player)


screen.listen()
screen.onkey(fun=paddle_right.up, key="Up")
screen.onkey(fun=paddle_right.down, key="Down")
screen.onkey(fun=paddle_left.up, key="w")
screen.onkey(fun=paddle_left.down, key="s")


game_is_on = True
while game_is_on:
    # Here, with time.sleep() method we are pausing/sleeping our while loop before the subsequent iteration
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with TOP/BOTTOM Walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce
        ball.bounce_y()

    # Detect collision with paddle_right and paddle_left
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.increment_score(side="left")

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.increment_score(side="right")


screen.exitonclick()
