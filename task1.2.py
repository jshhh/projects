import tkinter
from math import *
from random import *

SCREEN_SIZE = (600, 600)


def xs(x):
    return SCREEN_SIZE[0] // 2 + x
def oxs(x):
    return -SCREEN_SIZE[0] // 2 + x

def ys(y):
    return SCREEN_SIZE[1] // 2 - y
def oys(y):
    return -y+SCREEN_SIZE[1] // 2


main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=SCREEN_SIZE[1], width=SCREEN_SIZE[0])


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


class nugolnik:
    def __init__(self):
        self.ss = []
        self.ox = 0
        self.oy = 0
        self.alpha = 0
        self.item = None

    def rotate(self, alpha):
        # alpha
        ss1 = [0] * len(self.ss)
        ov = Vektor(x=self.ox, y=self.oy)
        for i in range(0, len(self.ss), 2):
            v = Vektor(x=self.ss[i], y=self.ss[i + 1])
            v = v - ov
            v = v.rotate(alpha)
            v = v + ov
            ss1[i] = v.x
            ss1[i + 1] = v.y
        return ss1

    def scale(self, k):
        ss1 = [0] * len(self.ss)
        ov = Vektor(x=self.ox, y=self.oy)
        for i in range(0, len(self.ss), 2):
            v = Vektor(x=self.ss[i], y=self.ss[i + 1])
            v = v - ov
            v.x *= k
            v.y *= k
            v = v + ov
            ss1[i] = v.x
            ss1[i + 1] = v.y
        return ss1

    def draw(self):
        ss1 = [0] * len(self.ss)
        for i in range(0, len(self.ss), 2):
            ss1[i]=xs(self.ss[i])
            ss1[i+1]=ys(self.ss[i+1])
        if len(self.ss)>0:
            if self.item is None:
                self.item = canvas.create_polygon(ss1, outline='red', fill='white')
            else:
                canvas.coords(self.item,ss1)
        return self.item

    def change_rotation_point(self,x,y):
        self.ox=oxs(x)
        self.oy=oys(y)

    def add_point(self,x,y):
        self.ss.append(oxs(x))
        self.ss.append(oys(y))
        self.draw()

poly = nugolnik()

def rotPoint(event):
    print(event)
    canvas.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill="red")
    poly.change_rotation_point(event.x,event.y)

def addPoint(event):
    poly.add_point(event.x,event.y)

canvas.bind('<Button-3>', rotPoint)
canvas.bind('<Button-1>', addPoint)
def leftKey(event):
    poly.ss = poly.rotate(-0.5)
    poly.draw()

def rightKey(event):
    poly.ss = poly.rotate(0.5)
    poly.draw()
def upKey(event):
    poly.ss = poly.scale(1.25)
    poly.draw()
def downKey(event):
    poly.ss = poly.scale(0.8)
    poly.draw()

def rotate(alpha, s):
    poly.draw()

main.bind('<Left>',leftKey)
main.bind('<Right>',rightKey)
main.bind('<Up>',upKey)
main.bind('<Down>',downKey)


canvas.pack()
main.mainloop()
