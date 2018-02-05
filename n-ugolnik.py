import tkinter
from math import *
from random import *

SCREEN_SIZE = (600, 600)


def xs(x):
    return SCREEN_SIZE[0] // 2 + x


def ys(y):
    return SCREEN_SIZE[1] // 2 - y


main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=SCREEN_SIZE[1], width=SCREEN_SIZE[0])
canvas.create_line((xs(0), ys(SCREEN_SIZE[1]//2)), xs(0), ys(-SCREEN_SIZE[1]//2), fill='#336699')
canvas.create_line((xs(-SCREEN_SIZE[0]//2), ys(0)), xs(SCREEN_SIZE[0]//2), ys(0), fill='black')

n = int(input('amount of angles: '))
l = int(input('side length: '))
alpha = int(input('starting angle: '))


# rotation of vector
def coords(x1, y1, alpha):
    alpha = alpha / 180 * pi
    x2 = x1 * cos(alpha) - y1 * sin(alpha)
    y2 = x1 * sin(alpha) + y1 * cos(alpha)
    return x2, y2


class Vektor:
    def __init__(self, x=None, y=None, l=None, a=None):
        if x is not None and y is not None:
            self.x = x
            self.y = y
        elif l is not None and a is not None:
            self.x = l
            self.y = 0
            if a != 0:
                v1 = self.rotate(a)
                self.x = v1.x
                self.y = v1.y

    def rotate(self, a):
        a = a / 180 * pi
        x = self.x * cos(a) - self.y * sin(a)
        y = self.x * sin(a) + self.y * cos(a)
        return Vektor(x, y)

    def __add__(self, other):
        if isinstance(other, Vektor):
            return Vektor(x=(self.x + other.x), y=(self.y + other.y))

    def __neg__(self):
        return Vektor(x=-self.x, y=-self.y)

    def __sub__(self, other):
        return self + (-other)


phi = 360 / n
radius = l / (2 * sin(phi / 360 * pi))
v0 = Vektor(l=radius, a=0)
v1 = Vektor(l=radius, a=0)

s = []
ss = []

for i in range(0, n):
    v2 = v1 - v0
    v2 = v2.rotate(180)
    s.append(v2.x)
    s.append(v2.y)
    ss.append(xs(v2.x))
    ss.append(ys(v2.y))
    v1 = v0.rotate(phi*(i+1))

l = canvas.create_polygon(ss, fill='#face8d')


# s = []
# ss = []
# s.append(0)
# s.append(0)
#
# for i in range(2, n * 2):
#     s.append(randint(50, 200))
#     if i % 2 == 0:
#         ss.append(xs(s[i]))
#     else:
#         ss.append(ys(s[i]))
#
# l = canvas.create_polygon(s, fill='red')


def rotate(alpha, s):
    ss = [0] * len(s)

    alpha += 1
    for j in range(n):
        v3 = Vektor(x=s[2 * j],y=s[2 * j + 1]).rotate(alpha)
        ss[2 * j], ss[2 * j + 1] = xs(v3.x), ys(v3.y)
    canvas.coords(l, ss)
    main.after(30, rotate, alpha, s)


rotate(alpha, s)
canvas.pack()
main.mainloop()
