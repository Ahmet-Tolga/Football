import turtle
pen=turtle.Screen()
pen.bgcolor("green")
pen.title("AMAZİNG futbol")
pen.setup(width=1000,height=600)

a=turtle.Turtle()
a.width(3)
a.speed(0)
a.penup()
a.goto(0,-90)
a.pendown()
a.color("white")
a.circle(100)
a.right(90)
a.forward(500)
a.backward(500)
a.penup()
a.backward(200)
a.pendown()
a.backward(500)

b=turtle.Turtle()
b.speed(0)
b.color("white")
b.width(5)
b.penup()
b.goto(-460,260)
b.pendown()
for i in range(2,6):
    if (i%2==0):
        b.forward(900)
        b.right(90)
    if (i%2==1):
        b.forward(500)
        b.right(90)
ball=turtle.Turtle()
ball.color("silver")
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(-480,0)
x=3
kale=turtle.Turtle()
kale.penup()
kale.speed(0)
kale.color("white")
kale.goto(480,0)
kale.shape("square")
kale.shapesize(10,5)

k=turtle.Turtle()
k.speed(0)
k.color("red")
k.shape("circle")
k.penup()
k.goto(350,0)
def f():
    y=20
    k.sety(k.ycor()+y)
def g():
    y=20
    k.sety(k.ycor()-y)
pen.listen()
pen.onkeypress(f,"o")
pen.onkeypress(g,"l")

def h():
    y=20
    ball.sety(ball.ycor()+y)
def z():
    y=20
    ball.sety(ball.ycor()-y)
pen.listen()
pen.onkeypress(h,"w")
pen.onkeypress(z,"s")
puan=0
puan2=0
l=turtle.Turtle()
l.speed(0)
l.color("black")
l.penup()
l.goto(-350,190)
l.write("puan:{}".format(puan),align="center",font=("courier",30,"normal"))

s=turtle.Turtle()
s.speed(0)
s.color("black")
s.penup()
s.goto(350,190)
s.write("puan:{}".format(puan2),align="center",font=("courier",30,"normal"))

while True:
    pen.update()
    ball.setx(ball.xcor()+3)

    if ball.xcor()>490:
        ball.goto(-480,0)
        puan+=10
        l.clear()
        l.write("puan:{}".format(puan), align="center", font=("courier", 30, "normal"))
    if (ball.distance(k)<20):
        puan2+=10
        s.clear()
        s.write("puan:{}".format(puan2), align="center", font=("courier", 30, "normal"))
        ball.goto(0,0)
    if (ball.ycor()<-50 or ball.ycor()>50):
        if (ball.xcor()>450):
            puan2+=10
            s.clear()
            s.write("puan:{}".format(puan2), align="center", font=("courier", 30, "normal"))
            ball.goto(0,0)


