from  turtle import  Turtle , Screen
import time
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.tracer(0)
screen.listen()

########Setting up of initial screen#######
net = Turtle()
net.color("grey")
net.goto(0,300)
net.setheading(270)
net.forward(600)

ball = Turtle(shape="circle")
ball.color("grey")
ball.penup()
ball.speed(4)
ball.setheading(random.randint(0,359))

p1_racket_segments=[]
for i in range(3):
    p1_new_segment = Turtle(shape = "square")
    p1_new_segment.speed("fastest")
    p1_new_segment.color("white")
    p1_new_segment.penup()
    p1_new_segment.goto(270,30)
    p1_new_segment.setheading(90)
    p1_new_segment.backward(20*i)
    p1_racket_segments.append(p1_new_segment)

    
p2_racket_segments=[]
for i in range(3):
    p2_new_segment = Turtle(shape = "square")
    p2_new_segment.speed("fastest")
    p2_new_segment.color("white")
    p2_new_segment.penup()
    p2_new_segment.goto(-270,30)
    p2_new_segment.setheading(90)
    p2_new_segment.backward(20*i)
    p2_racket_segments.append(p2_new_segment)


score_p1 = Turtle()
score_of_p1 = 0
score_p1.penup()
score_p1.color("white")
score_p1.hideturtle()
score_p1.goto(100,230)
score_p1.write(f"{score_of_p1} ", False, align = "center", font = ("Calibiri",45,"bold"))

score_p2 = Turtle()
score_of_p2 = 0
score_p2.penup()
score_p2.color("white")
score_p2.hideturtle()
score_p2.goto(-100,230)
score_p2.write(f"{score_of_p1} ", False, align = "center", font = ("Calibiri",45,"bold"))
screen.update()
time.sleep(0.5)

result = Turtle()
result.penup()
result.ht()
result.color("white")

 #####Keybinding The Rackets####
def move_up_p1():
    for segments in p1_racket_segments:
        segments.setheading(90)
        segments.forward(10)
    
def move_down_p1():
    for segments in p1_racket_segments:
        segments.setheading(270)
        segments.forward(10)
    
def move_up_p2():
    for segments in p2_racket_segments:
        segments.setheading(90)
        segments.forward(10)
    
def move_down_p2():
    for segments in p2_racket_segments:
        segments.setheading(270)
        segments.forward(10)
    
is_game_on = True

while is_game_on:
    #####Racket Movement#####
    screen.onkeypress(fun = move_up_p1,key="Up")
    screen.onkeypress(fun = move_down_p1, key="Down")
    screen.onkeypress(fun = move_up_p2, key="w")
    screen.onkeypress(fun = move_down_p2, key="s")

    if p1_racket_segments[0].ycor()>=290:
        screen.onkeypress(fun = None, key="Up")
    if p1_racket_segments[-1].ycor()<=-290:
        screen.onkeypress(fun = None, key="Down")
    if p2_racket_segments[0].ycor()>=290:
        screen.onkeypress(fun = None, key="w")
    if p2_racket_segments[-1].ycor()<=-290:
        screen.onkeypress(fun = None, key="s")
    screen.update()
    time.sleep(0.01)

    ball.forward(21)
    screen.update()
    time.sleep(0.1)

    for segments_p1 in p1_racket_segments:
        if ball.distance(segments_p1)<=20:
            ball.setheading(random.randint(90,270))
            screen.update()
            time.sleep(0.01)
        else:
            pass
    for segments_p2 in p2_racket_segments:
        if ball.distance(segments_p2)<=20:
            ball.setheading(random.randint(270,450))
            screen.update()
            time.sleep(0.01)
        else:
            pass
    

    if ball.xcor()>300:
        score_of_p2 +=1
        score_p2.clear()
        score_p2.write(f"{score_of_p2} ", False, align = "center", font = ("Calibiri",45,"bold"))
        if score_of_p2<5 and score_of_p1<5:
            ball.home()
            ball.setheading(random.randint(0,359))
            screen.update()
            time.sleep(1)

    elif ball.xcor()<-300:
        score_of_p1 +=1
        score_p1.clear()
        score_p1.write(f"{score_of_p1} ", False, align = "center", font = ("Calibiri",45,"bold"))
        if score_of_p2<5 and score_of_p1<5:
            ball.home()
            ball.setheading(random.randint(0,359))
            screen.update()
            time.sleep(1)
    
    if  ball.ycor()>280:
        if 90<=ball.heading()<180:
            ball.setheading(random.randint(190,260))
        elif 0<=ball.heading()<90:
            ball.setheading(random.randint(280,350))
        screen.update()
        time.sleep(0.1)
    elif ball.ycor()<-280:
        if 180<=ball.heading()<270:
            ball.setheading(random.randint(100,170))
        elif 270<=ball.heading()<360 :
            ball.setheading(random.randint(10,80))
        screen.update()
        time.sleep(0.01)
    
    if score_of_p1 ==5:
        is_game_on = False
        ball.ht()
        net.clear()
        result.write("        Player2 lost T.T\nPlayer1 is the Ultimate Winner", False, align = "center", font = ("Calibiri",20,"bold"))
        screen.update()
        time.sleep(10)
        result.clear()
        result.write("    To Play The Game Again\nPlease Run the Program Again.", False, align = "center", font = ("Calibiri",20,"bold"))

    elif score_of_p2 ==5:
        is_game_on = False
        ball.ht()
        net.clear()
        result.write("        Player1 lost T.T\nPlayer2 is the Ultimate Winner", False, align = "center", font = ("Calibiri",20,"bold"))
        screen.update()
        time.sleep(10)
        result.clear()
        result.write("    To Play The Game Again\nPlease Run the Program Again.", False, align = "center", font = ("Calibiri",20,"bold"))

        
screen.exitonclick()