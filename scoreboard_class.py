from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

class ScoreBoard(Turtle):
    def __init__(self, left_player, right_player):
        super().__init__()
        self.left_player = left_player
        self.right_player = right_player
        self.hideturtle()
        self.color("white")
        self.teleport(y=280)
        self.score_left = 0
        self.score_right = 0
        self.update_score()

    def update_score(self):
        self.write(F"{self.left_player} {self.score_left}-{self.score_right} {self.right_player}", align=ALIGNMENT, font=FONT)

    def increment_score(self, side):
        if side == "left":
            self.score_left += 1
        elif side == "right":
            self.score_right += 1

        self.clear()
        self.update_score()
