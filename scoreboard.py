from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_Score=0
        self.r_score=0
        self.upgrade_Score()
    def upgrade_Score(self):
        self.clear()
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",70,"normal"))
        self.goto(-100,200)
        self.write(self.l_Score,align="center",font=("Courier",70,"normal"))
    def l_plus(self):
        self.l_Score+=1
        self.upgrade_Score()
    def r_plus(self):
        self.r_score+=1
        self.upgrade_Score()