from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.listen()
is_game=True
positions=[(-360,0),(360,0)]
l_paddle=Paddle(positions[0])
r_paddle=Paddle(positions[1])

score=Scoreboard()

screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(key="w",fun=l_paddle.go_up)
screen.onkey(key="s",fun=l_paddle.go_down)

ball=Ball()


while is_game==True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() == -280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        score.l_plus()
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_plus()










screen.exitonclick()
