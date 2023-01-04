import turtle as t


def A():
    t.goto(t.xcor()+6, t.ycor()+24)
    t.goto(t.xcor()+3, t.ycor()-12)
    t.goto(t.xcor()-6, t.ycor())
    t.goto(t.xcor()+6, t.ycor())
    t.goto(t.xcor()+3, t.ycor()-12)

def B():
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor()+6, t.ycor())
    t.circle(-6, 180)
    t.goto(t.xcor()-6, t.ycor())
    t.goto(t.xcor()+6, t.ycor())
    t.circle(6, -180)
    t.goto(t.xcor()-6, t.ycor())
    t.pu()
    t.goto(t.xcor()+12, t.ycor())

def C():
    t.up()
    t.goto(t.xcor()+12, t.ycor()+24)
    t.pd()
    t.circle(-12, -180)
    

def D():
    t.circle(12, 180)
    t.goto(t.xcor(), t.ycor()-24)
    t.pu()
    t.goto(t.xcor()+12, t.ycor())

def E():
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor()+12, t.ycor())
    t.pu()
    t.goto(t.xcor()-4, t.ycor()-12)
    t.pd()
    t.goto(t.xcor()-8, t.ycor())
    t.goto(t.xcor(), t.ycor()-12)
    t.goto(t.xcor()+12, t.ycor())

def F():
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor()+12, t.ycor())
    t.pu()
    t.goto(t.xcor()-4, t.ycor()-12)
    t.pd()
    t.goto(t.xcor()-8, t.ycor())
    t.pu()
    t.goto(t.xcor()+12, t.ycor()-12)

def G():
    t.up()
    t.goto(t.xcor()+12, t.ycor()+24)
    t.pd()
    t.circle(-12, -180)
    t.goto(t.xcor(), t.ycor()+12)
    t.goto(t.xcor()-6, t.ycor())
    t.pu()
    t.goto(t.xcor()+6, t.ycor()-12)

def H():
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor(), t.ycor()-12)
    t.goto(t.xcor()+12, t.ycor())
    t.goto(t.xcor(), t.ycor()+12)
    t.goto(t.xcor(), t.ycor()-24)

def I():
    t.pu()
    t.goto(t.xcor(), t.ycor()+24)
    t.pd()
    t.goto(t.xcor()+12, t.ycor())
    t.goto(t.xcor()-6, t.ycor())
    t.goto(t.xcor(), t.ycor()-24)
    t.goto(t.xcor()-6, t.ycor())
    t.goto(t.xcor()+12, t.ycor())

def J():
    t.pu()
    t.goto(t.xcor(), t.ycor()+24)
    t.pd()
    t.goto(t.xcor()+12, t.ycor())
    t.goto(t.xcor(), t.ycor()-18)
    t.setheading(90)
    t.circle(6, -180)
    t.pu()
    t.goto(t.xcor()+12, t.ycor()-6)

def K():
    t.goto(t.xcor(), t.ycor()+24)
    t.pu()
    t.goto(t.xcor()+12, t.ycor())
    t.pd()
    t.goto(t.xcor()-12, t.ycor()-12)
    t.goto(t.xcor()+12, t.ycor()-12)

def L():
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor(), t.ycor()-24)
    t.goto(t.xcor()+12, t.ycor())
    
def M():
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor()+6, t.ycor()-12)
    t.goto(t.xcor()+6, t.ycor()+12)
    t.goto(t.xcor(), t.ycor()-24)

def N():
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor()+12, t.ycor()-24)    
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor(), t.ycor()-24)

def O():
    t.pu()
    t.goto(t.xcor(), t.ycor()+6)
    t.seth(270)
    t.pd()
    t.circle(6, 180)
    t.goto(t.xcor(), t.ycor()+12)
    t.circle(6, 180)
    t.goto(t.xcor(), t.ycor()-12)
    t.pu()
    t.goto(t.xcor()+12, t.ycor()-6)

def P():
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor()+6, t.ycor())
    t.circle(-6, 180)
    t.goto(t.xcor()-6, t.ycor())
    t.pu()
    t.goto(t.xcor()+12, t.ycor()-12)

def Q():
    t.pu()
    t.goto(t.xcor(), t.ycor()+6)
    t.setheading(270)
    t.pd()
    t.circle(6, 180)
    t.goto(t.xcor(), t.ycor()+12)
    t.circle(6, 180)
    t.goto(t.xcor(), t.ycor()-12)
    t.pu()
    t.goto(t.xcor()+6, t.ycor())
    t.pd()
    t.goto(t.xcor()+6, t.ycor()-6)

def R():
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor()+6, t.ycor())
    t.circle(-6, 180)
    t.goto(t.xcor()-6, t.ycor())
    t.goto(t.xcor()+6, t.ycor())
    t.goto(t.xcor()+6, t.ycor()-12)

def S():
    t.goto(t.xcor()+6, t.ycor())
    t.circle(6, 180)
    t.circle(-6, 180)
    t.goto(t.xcor()+6, t.ycor())
    t.pu()
    t.goto(t.xcor(), t.ycor()-24)

def T():
    t.pu()
    t.goto(t.xcor()+6, t.ycor())
    t.pd()
    t.goto(t.xcor(), t.ycor()+24)
    t.goto(t.xcor()-6, t.ycor())
    t.goto(t.xcor()+12, t.ycor())
    t.pu()
    t.goto(t.xcor(), t.ycor()-24)

def U():
    t.pu()
    t.goto(t.xcor(), t.ycor()+24)
    t.pd()
    t.goto(t.xcor(), t.ycor()-18)
    t.seth(90)
    t.circle(-6, -180)
    t.goto(t.xcor(), t.ycor()+18)
    t.goto(t.xcor(), t.ycor()-24)

def V():
    t.pu()
    t.goto(t.xcor(), t.ycor()+24)
    t.pd()
    t.goto(t.xcor()+6, t.ycor()-24)
    t.goto(t.xcor()+6, t.ycor()+24)
    t.pu()
    t.goto(t.xcor(), t.ycor()-24)

def W():
    t.pu()
    t.goto(t.xcor(), t.ycor()+24)
    t.pd()
    t.goto(t.xcor()+3, t.ycor()-24)
    t.goto(t.xcor()+3, t.ycor()+12)
    t.goto(t.xcor()+3, t.ycor()-12)
    t.goto(t.xcor()+3, t.ycor()+24)
    t.pu()
    t.goto(t.xcor(), t.ycor()-24)

def X():
    t.goto(t.xcor()+12, t.ycor()+24)
    t.pu()
    t.goto(t.xcor()-12, t.ycor())
    t.pd()
    t.goto(t.xcor()+12, t.ycor()-24)

def Y():
    t.pu()
    t.goto(t.xcor()+6, t.ycor())
    t.pd()
    t.goto(t.xcor(), t.ycor()+12)
    t.goto(t.xcor()-6, t.ycor()+12)
    t.goto(t.xcor()+6, t.ycor()-12)
    t.goto(t.xcor()+6, t.ycor()+12)
    t.pu()
    t.goto(t.xcor(), t.ycor()-24)

def Z():
    t.pu()
    t.goto(t.xcor(), t.ycor()+24)
    t.pd()
    t.goto(t.xcor()+12, t.ycor())
    t.goto(t.xcor()-12, t.ycor()-24)
    t.goto(t.xcor()+12, t.ycor())
