import turtle
pointer= turtle.Turtle()
pointer.speed(0.51)
pointer.screen.setup(width=1000,height=550)
pointer.screen.bgcolor("red")
pointer.hideturtle()

def star(size):
    pointer.penup()
    pointer.goto(77,64)
    pointer.pendown()
    pointer.color("white")
    pointer.begin_fill()
    pointer.pencolor("white")
    for i in range(5):
        if i==0:
           angle=125
        else:
            angle=144
        pointer.right(angle)
        pointer.forward(size)
    pointer.end_fill()

pointer.penup()
pointer.goto(-175,-130)
pointer.pendown()
pointer.color("white")
pointer.begin_fill()
pointer.circle(150)
pointer.end_fill()
pointer.color("red")
pointer.begin_fill()
pointer.penup()
pointer.goto(-140,-99)
pointer.pendown()
pointer.circle(120)
pointer.circle(120)     
pointer.end_fill()


star(130)


pointer.screen.mainloop()
