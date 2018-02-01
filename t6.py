import tkinter
from math import *

SCREEN_SIZE = (600, 600)


def xs(x):
    return SCREEN_SIZE[0] // 2 + x


def ys(y):
    return SCREEN_SIZE[1] // 2 - y


main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=600, width=600)
canvas.create_line((xs(0), ys(400)), xs(0), ys(-400), fill='black')
canvas.create_line((xs(-400), ys(0)), xs(400), ys(0), fill='black')
s = int(input())
alpha = int(input())


def coords(x1, y1, alpha):
    alpha = alpha / 180 * pi
    x2 = x1 * cos(alpha) - y1 * sin(alpha)
    y2 = x1 * sin(alpha) - y1 * cos(alpha)
    return x2, y2


def coords2(s, alpha):
    x0 = 0
    y0 = 0
    x1 = s
    y1 = 0
    x1, y1 = coords(x1, y1, alpha)
    x2 = -y1
    y2 = x1
    x3 = x1 - y1
    y3 = x1 + y1
    return x0, y0, x1, y1, x2, y2, x3, y3


x0, y0, x1, y1, x2, y2, x3, y3 = coords2(s,alpha)


l1 = canvas.create_line((xs(x0), ys(y0)), xs(x1), ys(y1), fill='black', width=4)
l2 = canvas.create_line((xs(x0), ys(y0)), xs(x2), ys(y2), fill='black', width=4)
l3 = canvas.create_line((xs(x2), ys(y2)), xs(x3), ys(y3), fill='black', width=4)
l4 = canvas.create_line((xs(x1), ys(y1)), xs(x3), ys(y3), fill='black', width=4)


def square(alpha):
    x0, y0, x1, y1, x2, y2, x3, y3 = coords2(s, alpha)
    canvas.coords(l1,xs(x0), ys(y0), xs(x1), ys(y1))
    canvas.coords(l2, xs(x0), ys(y0), xs(x2), ys(y2))
    canvas.coords(l3,xs(x2), ys(y2), xs(x3), ys(y3))
    canvas.coords(l4,xs(x1), ys(y1), xs(x3), ys(y3))
    alpha+=1
    print(alpha)
    main.after(10, square, alpha)

square(alpha)
canvas.pack()
main.mainloop()

