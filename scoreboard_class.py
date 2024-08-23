from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0

    def increment_score(self, side):
        if side == "left":
            self.score_left += 1
        elif side == "right":
            self.score_right += 1
