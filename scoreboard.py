import turtle
from turtle import Turtle
ALIGMENT = 'center'
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updatescoreboard()

    def updatescoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updatescoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALIGMENT, font=FONT)