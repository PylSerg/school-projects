from tkinter import *

bfs = "Arial 14 bold"

root = Tk()
root.title("Калькулятор")
root.geometry("260x380")
root.resizable(False, False)


# Створення віджетів
entry = Entry(root, font="Arial 14 normal", justify="right")

button_c = Button(root, text="C", font=bfs)
button_equal = Button(root, text="=", font=bfs)

button_divide = Button(root, text="/", font=bfs)
button_multiply = Button(root, text="*", font=bfs)
button_minus = Button(root, text="-", font=bfs)
button_plus = Button(root, text="+", font=bfs)

button_point = Button(root, text=".", font=bfs)

button_0 = Button(root, text="0", font=bfs)
button_1 = Button(root, text="1", font=bfs)
button_2 = Button(root, text="2", font=bfs)
button_3 = Button(root, text="3", font=bfs)
button_4 = Button(root, text="4", font=bfs)
button_5 = Button(root, text="5", font=bfs)
button_6 = Button(root, text="6", font=bfs)
button_7 = Button(root, text="7", font=bfs)
button_8 = Button(root, text="8", font=bfs)
button_9 = Button(root, text="9", font=bfs)


# Розміщення віджетів
entry.place(x=20, y=20, width=220, height=40)

button_c.place(x=20, y=80, width=100, height=40)
button_equal.place(x=140, y=80, width=100, height=40)

root.mainloop()