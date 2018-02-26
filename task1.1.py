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
# k=float(input())
# n=int(input())
# n1=int(input())
# l = int(input('side length: '))
# xp=int(input())
# yp=int(input())

k=int(input('коэфициент:'))
n=int(input('кол-во углов'))
n1=int(input())
l = int(input())
def coordsx(k,xp,xs):
    xq = xs+k*(xp-xs)
    return xq
def coordsy(k,yp,ys):
    yq = ys + k * (yp-ys)
    return  yq

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

l = canvas.create_polygon(ss, outline = 'red',fill = 'white')
def mashtab(ss,k,xp,yp):
    ss1 = [0]*len(ss);
    for i in range(0,len(ss),2):
        ss1[i]=coordsx(k,ss[(i+2)%len(ss)],ss[i])
        ss1[i+1]=coordsy(k,ss[(i+3)%len(ss)],ss[i+1])
    return ss1
for j in range(n1):
    ss=mashtab(ss,k,xp,yp)
    canvas.create_polygon(ss, outline = 'red',fill = 'white')
canvas.pack()
main.mainloop()