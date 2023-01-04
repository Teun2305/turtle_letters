import turtle as t


def space():
    t.pu()
    t.goto(t.xcor()+12, t.ycor())

def enter():
    t.pu()
    t.goto(-t.window_width()//2, t.ycor()-30)

def dot():
    t.pu()
    t.goto(t.xcor()+1, t.ycor()+1)
    t.pd()
    t.dot(3)
    t.pu()
    t.goto(t.xcor()+11, t.ycor()-1)

def comma():
    t.pu()
    t.goto(t.xcor()-1, t.ycor()-1)
    t.pd()
    t.goto(t.xcor()+4, t.ycor()+4)
    t.pu()
    t.goto(t.xcor()-9, t.ycor()-3)

def apos():
    t.pu()
    t.goto(t.xcor()-5, t.ycor()+20)
    t.pd()
    t.goto(t.xcor()+4, t.ycor()+4)
    t.pu()
    t.goto(t.xcor()-5, t.ycor()-24)

def hyphen():
    t.pu()
    t.goto(t.xcor(), t.ycor()+12)
    t.pd()
    t.goto(t.xcor()+12, t.ycor())
    t.pu()
    t.goto(t.xcor(), t.ycor()-12)

def colon():
    t.pu()
    t.goto(t.xcor()+6, t.ycor()+8)
    t.pd()
    t.circle(1)
    t.pu()
    t.goto(t.xcor(), t.ycor()+8)
    t.pd()
    t.circle(1)
    t.pu()
    t.goto(t.xcor()+6, t.ycor()-16)

def emptyset():
    t.pu()
    t.goto(t.xcor(), t.ycor()+6)
    t.seth(270)
    t.pd()
    t.circle(6, 180)
    t.goto(t.xcor(), t.ycor()+12)
    t.circle(6, 180)
    t.goto(t.xcor(), t.ycor()-12)
    t.pu()
    t.goto(t.xcor(), t.ycor()-6)
    t.pd()
    t.goto(t.xcor()+12, t.ycor()+24)
    t.pu()
    t.goto(t.xcor(), t.ycor()-24)

def et():
    t.pu()
    t.goto(t.xcor()+12, t.ycor()+8)
    t.seth(90)
    t.pd()
    t.goto(t.xcor(), t.ycor()-2)
    t.circle(6, -225)
    t.goto(t.xcor()+6.07, t.ycor()+4.93)
    t.circle(-4, -270)
    t.goto(t.xcor()+9.83, t.ycor()-15.17)
