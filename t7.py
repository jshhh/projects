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

    r=2*a*(1-cos(alpha))
    x=r*cos(alpha)
    y=r*sin(alpha)
    canvas.create_line((xs(x1), ys(y1)), xs(x), ys(y), fill='black')
    alpha+=0.05
    main.after(10, square, alpha,x,y)

square(alpha,0,0)
canvas.pack()
main.mainloop()