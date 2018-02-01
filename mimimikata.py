import tkinter
from math import *
from random import *

SCREEN_SIZE = (600, 600)


def xs(x):
    return SCREEN_SIZE[0] // 2 + x


def ys(y):
    return SCREEN_SIZE[1] // 2 - y


x = input()


main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=600, width=600)
canvas.create_line((xs(0), ys(400)), xs(0), ys(-400), fill='black')
canvas.create_line((xs(-400), ys(0)), xs(400), ys(0), fill='black')
n = int(input())
alpha = int(input())


def coords(x1, y1, alpha):
    alpha = alpha / 180 * pi
    x2 = x1 * cos(alpha) - y1 * sin(alpha)
    y2 = x1 * sin(alpha) + y1 * cos(alpha)
    return x2, y2


f - -f
s = []
ss = []
s.append(0)
s.append(0)
for i in range(2, n * 2):
    s.append(randint(50, 200))
    if i % 2 == 0:
        ss.append(xs(s[i]))
    else:
        ss.append(ys(s[i]))

l = canvas.create_polygon(s, fill='red')


def square(alpha, s):
    ss = [0] * len(s)

    alpha += 1
    for j in range(n):
        x, y = coords(s[2 * j], s[2 * j + 1], alpha)
        ss[2 * j], ss[2 * j + 1] = xs(x), ys(y)
    canvas.coords(l, ss)
    main.after(30, square, alpha, s)


square(alpha, s)
canvas.pack()
main.mainloop()
