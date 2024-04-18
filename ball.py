from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 0.05
        self.y_move = 0.05

    def create_ball(self):
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(0.7, 0.7)

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move = -self.y_move

    def hit(self):
        self.x_move = -self.x_move

    def point(self):
        self.home()
        self.bounce()
        self.hit()
