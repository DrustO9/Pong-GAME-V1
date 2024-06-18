from turtle import Turtle


class Paddle:
    def __init__(self, x_cord, y_cord):
        self.paddle = Turtle()
        self.x_cordinate = x_cord
        self.y_cordinate = y_cord
        self.create_paddle()

    def create_paddle(self):
        self.paddle = Turtle()
        self.paddle.turtlesize(stretch_wid=1, stretch_len=5)
        self.paddle.setheading(90)
        self.paddle.shape("square")
        self.paddle.penup()
        self.paddle.goto(self.x_cordinate, self.y_cordinate)
        self.paddle.color("white")

    def move_up(self):
        self.paddle.forward(40)

    def move_down(self):
        self.paddle.backward(40)
