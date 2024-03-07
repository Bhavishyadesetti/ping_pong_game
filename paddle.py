from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()

        self.shape("square")

        self.resizemode("user")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.color("white")
        self.goto(x=position[0], y=position[1])

    def go_up(self):
        self.forward(30)

    def go_down(self):
        self.backward(30)
