import tkinter

SCREEN_SIZE = [500, 500]

main = tkinter.Tk()
main.title("Mouse events. Motion. Buttons")
coords=[]
kruzhochki=[]
def motion(event):
    label.configure(text="Mouse position: (%d, %d)" % (event.x, event.y))
    return

precision = int(input('input precision in px: '))


def narisovat_krivuliaku(coords):
    x = -SCREEN_SIZE[0]//2
    y = lagrange(coords,x)
    for newx in range(0,SCREEN_SIZE[0],precision):
        newy = lagrange(coords,newx);
        canvas.create_line(x,y,newx,newy,fill='red')
        x=newx
        y=newy
    pass


def press(event):
    kruzhochki.append(canvas.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill="red"))

    for i in range(1,len(coords),2):
        if coords[i]==event.y:
            print ('y is ambigous')
            return
        if coords[i-1]==event.x:
            print ('x is ambigous')
            return

    coords.append(event.x)
    coords.append(event.y)
    if len(coords)>2*2:
        narisovat_krivuliaku(coords)
    return

def delpoint(event):
    canvas.delete(kruzhochki.pop())
    coords.pop()
    coords.pop()
    if len(coords)>2*2:
        narisovat_krivuliaku(coords)
    return


canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
canvas.bind('<Motion>', motion)
canvas.bind('<Button 1>', press)
canvas.bind('<Button 3>', delpoint)
canvas.pack()


label = tkinter.Label(main, text="Mouse position (0, 0): ")
label.pack()

# нарисуем оси
canvas.create_line(0, SCREEN_SIZE[1] // 2, SCREEN_SIZE[0], SCREEN_SIZE[1] // 2)
canvas.create_line(SCREEN_SIZE[0] // 2, 0, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1])

def lagrange1(coords,x,i):
    f=1
    for j in range(0,len(coords),2):
        if i!=j:
            f *= (x-coords[j])/(coords[i]-coords[j])
    return f

def lagrange(coords,x):
    sum = 0
    for i in range(1,len(coords),2):
        li = lagrange1(coords,x,i-1)
        sum += coords[i]*li
    return sum




main.mainloop()
