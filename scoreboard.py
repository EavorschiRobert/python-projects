from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open('./data.txt') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 24, 'normal'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('./data.txt', 'w') as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        # self.write(f"GAME OVER", align='center', font=('Arial', 24, 'normal'))
