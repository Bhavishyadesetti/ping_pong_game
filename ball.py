from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.resizemode("user")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.penup()
        self.move_speed=0.1
        self.x_mo = 10
        self.y_mo = 10
        self.move()



    def move(self):
        x_c=self.xcor()+self.x_mo
        y_c=self.ycor()+self.y_mo
        self.goto(x=x_c,y=y_c)
    def bounce_y(self):
        self.y_mo *=-1
        self.move_speed*=0.9
    def bounce_x(self):
        self.x_mo*=-1
        self.move_speed*=0.9

    def reset_position(self):
        self.move_speed=0.1
        self.goto(0,0)
        self.bounce_x()









