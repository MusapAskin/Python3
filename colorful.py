import turtle

colors = ['red','orange','yellow','green','blue','indigo','violet']
t = turtle.Pen()
t.speed(300)
turtle.bgcolor("black")
for x in range(700):
    t.pencolor(colors[x%7])
    t.width(x/100+1)
    t.forward(x)
    t.left(50)
    
turtle.done()
