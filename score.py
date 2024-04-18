from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.scores = [0, 0]
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.scores[0], align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.scores[1], align='center', font=('Courier', 80, 'normal'))

    def add_point(self, player):
        if player == 1:
            self.scores[0] += 1
        else:
            self.scores[1] += 1
        self.clear()
        self.update_score()
