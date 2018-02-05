import tkinter
from math import *

SCREEN_SIZE = (600, 600)


def xs(x):
    return SCREEN_SIZE[0] // 2 + x


def ys(y):
    return SCREEN_SIZE[1] // 2 - y

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=600, width=600)
a = int(input())
alpha = int(input())
def square(alpha,x1,y1):
    q=a**2*cos(2*alpha)
    if q>=0:
        r=sqrt(q)
    else:
        r=sqrt(-q)
    x=r*cos(alpha)
    y=r*sin(alpha)
    if x1 is not None :
        canvas.create_line((xs(x1), ys(y1)), xs(x), ys(y), fill='black')
    alpha+=0.05
    main.after(10, square, alpha,x,y)

square(alpha,None,None)
canvas.pack()
main.mainloop()