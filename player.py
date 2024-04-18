from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_players(position)

    def create_players(self, position):
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position, 0)
        self.color('white')

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
