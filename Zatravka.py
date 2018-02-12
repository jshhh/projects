import tkinter

SCREEN_SIZE = [500, 500]

main = tkinter.Tk()
main.title("Mouse events. Motion. Buttons")

canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
canvas.pack()

# нарисуем оси
canvas.create_line(0, SCREEN_SIZE[1] // 2, SCREEN_SIZE[0], SCREEN_SIZE[1] // 2)
canvas.create_line(SCREEN_SIZE[0] // 2, 0, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1])

main.mainloop()
