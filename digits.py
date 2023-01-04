import turtle as t


def one():
    t.pu()
    t.goto(t.xcor(), t.ycor()+18)
    t.pd()
    t.goto(t.xcor()+6, t.ycor()+6)
    t.goto(t.xcor(), t.ycor()-24)
    t.goto(t.xcor()-6, t.ycor())
    t.goto(t.xcor()+12, t.ycor())

def two():
    t.pu()
    t.goto(t.xcor(), t.ycor()+18)
    t.pd()
    t.seth(90)
    t.circle(-6, 180)
    t.goto(t.xcor()-12, t.ycor()-18)
    t.goto(t.xcor()+12, t.ycor())

def three():
    t.goto(t.xcor()+6, t.ycor())
    t.circle(6, 180)
    t.goto(t.xcor()-3, t.ycor())
    t.goto(t.xcor()+3, t.ycor())
    t.circle(-6, -180)
    t.goto(t.xcor()-6, t.ycor())
    t.pu()
    t.goto(t.xcor()+12, t.ycor()-24)

def four():
    t.pu()
    t.goto(t.xcor()+8, t.ycor())
    t.pd()
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor()-8, t.ycor()-16)
    t.goto(t.xcor()+12, t.ycor())
    t.pu()
    t.goto(t.xcor(), t.ycor()-8)

def five():
    t.goto(t.xcor()+5, t.ycor())
    t.circle(7, 180)
    t.goto(t.xcor()-5, t.ycor())
    t.goto(t.xcor(), t.ycor()+10)
    t.goto(t.xcor()+12, t.ycor())
    t.pu()
    t.goto(t.xcor(), t.ycor()-24)

def six():
    t.pu()
    t.goto(t.xcor(), t.ycor()+6)
    t.seth(270)
    t.pd()
    t.circle(6, 180)
    t.goto(t.xcor(), t.ycor()+3)
    t.circle(6, 180)
    t.goto(t.xcor(), t.ycor()-3)
    t.goto(t.xcor(), t.ycor()+12)
    t.circle(6, -180)
    t.pu()
    t.goto(t.xcor(), t.ycor()-18)

def seven():
    t.pu()
    t.goto(t.xcor(), t.ycor()+24)
    t.pd()
    t.goto(t.xcor()+12, t.ycor())
    t.goto(t.xcor()-12, t.ycor()-24)
    t.pu()
    t.goto(t.xcor()+12, t.ycor())

def eight():
    t.pu()
    t.goto(t.xcor()+6, t.ycor())
    t.pd()
    t.circle(6, 360)
    t.pu()
    t.goto(t.xcor(), t.ycor()+12)
    t.pd()
    t.circle(6, 360)
    t.pu()
    t.goto(t.xcor()+6, t.ycor()-12)

def nine():
    t.seth(90)
    t.pu()
    t.goto(t.xcor(), t.ycor()+6)
    t.pd()
    t.circle(-6, -180)
    t.goto(t.xcor(), t.ycor()+12)
    t.circle(-6, -180)
    t.goto(t.xcor(), t.ycor()-3)
    t.circle(-6, -180)
    t.pu()
    t.goto(t.xcor(), t.ycor()-15)
