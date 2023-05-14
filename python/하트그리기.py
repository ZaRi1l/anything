import turtle as t

t.speed()
t.color('red')
t.width(30)
t.left(90)
for a in range(35):
    t.right(6)
    t.forward(6)
for a in range(25):
    t.right(a*0.2)
    t.forward(6)
t.penup()

t.home()
t.pendown()
t.setheading(90)
for a in range(35):
    t.left(6)
    t.forward(6)
for a in range(25):
    t.left(a*0.2)
    t.forward(6)

t.width(1)
t.penup()
t.begin_fill()
t.color('pink')

t.home()
t.pendown()
t.left(90)
for a in range(35):
    t.right(6)
    t.forward(6)
for a in range(24):
    t.right(a*0.2)
    t.forward(6)
t.penup()

t.home()

t.color('pink')
t.pendown()
t.setheading(90)
for a in range(35):
    t.left(6)
    t.forward(6)
for a in range(25):
    t.left(a*0.2)
    t.forward(6)

t.end_fill()


t.setheading(90)
t.forward(7)
t.width(16)
t.forward(90)
t.backward(15)
t.penup

t.color("red")
t.write("I LOVE YOU", move=False, align="center", font=("arial",23,"bold"))
t.color('pink')
t.backward(38)
t.color('red')
t.write("사랑해", move=False, align="center", font=("arial",23,"bold"))
t.hideturtle()

t.mainloop()