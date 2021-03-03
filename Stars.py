from turtle import *
import random
import threading
speed(speed='fastest')
def draw(n,x,angle):
    for i in range(n):
        bgcolor('black')
        colormode(255)
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255)

        pencolor(a,b,c)
        fillcolor(a,b,c)
        begin_fill()

        for j in range(5):
            forward(5*n-5*j)
            right(x)
            forward(5*n-5*j)
            right(72-x)

        end_fill()
        rt(angle)

n=30
x=144
angle=18
th = threading.Thread(target=draw(n,x,angle))
th.start()
exit(input())