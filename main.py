from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG game")
screen.bgcolor("black")
screen.tracer(0)
# Tracer controls animation

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with Top amd Bottom Wall

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_vertical()

    # detect collision with the Right paddle

    if ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 330:
        ball.bounce_horizontal()

    # detect collision with the left paddle

    if ball.distance(l_paddle.paddle) < 50 and ball.xcor() < -330:
        ball.bounce_horizontal()

    # detect missing collision with the Right paddle

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


        # detect missing collision with the Left paddle

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()
