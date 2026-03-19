from tkinter import *

bfs = "Arial 14 bold"

action = ""
a = ""
b = ""


def select_action(act):
    global action, a
    
    a = entry.get()
    action = act
    entry.delete(0, END)


def calc():
    global a, b
    
    b = entry.get()
    entry.delete(0, END)
    
    a = float(a)
    b = float(b)
    
    if action == "/" : entry.insert(END, a / b)
    if action == "*" : entry.insert(END, a * b)
    if action == "-" : entry.insert(END, a - b)
    if action == "+" : entry.insert(END, a + b)


root = Tk()
root.title("Калькулятор")
root.geometry("260x380")
root.resizable(False, False)


# Створення віджетів
entry = Entry(root, font="Arial 14 normal", justify="right")

button_c = Button(root, text="C", font=bfs, command=lambda: entry.delete(0, END))
button_equal = Button(root, text="=", font=bfs, command=calc)

button_divide = Button(root, text="/", font=bfs, command=lambda: select_action("/"))
button_multiply = Button(root, text="*", font=bfs, command=lambda: select_action("*"))
button_minus = Button(root, text="-", font=bfs, command=lambda: select_action("-"))
button_plus = Button(root, text="+", font=bfs, command=lambda: select_action("+"))

button_point = Button(root, text=".", font=bfs, command=lambda: entry.insert(END, "."))

button_0 = Button(root, text="0", font=bfs, command=lambda: entry.insert(END, "0"))
button_1 = Button(root, text="1", font=bfs, command=lambda: entry.insert(END, "1"))
button_2 = Button(root, text="2", font=bfs, command=lambda: entry.insert(END, "2"))
button_3 = Button(root, text="3", font=bfs, command=lambda: entry.insert(END, "3"))
button_4 = Button(root, text="4", font=bfs, command=lambda: entry.insert(END, "4"))
button_5 = Button(root, text="5", font=bfs, command=lambda: entry.insert(END, "5"))
button_6 = Button(root, text="6", font=bfs, command=lambda: entry.insert(END, "6"))
button_7 = Button(root, text="7", font=bfs, command=lambda: entry.insert(END, "7"))
button_8 = Button(root, text="8", font=bfs, command=lambda: entry.insert(END, "8"))
button_9 = Button(root, text="9", font=bfs, command=lambda: entry.insert(END, "9"))


# Розміщення віджетів
entry.place(x=20, y=20, width=220, height=40)

button_c.place(x=20, y=80, width=100, height=40)
button_equal.place(x=140, y=80, width=100, height=40)

button_7.place(x=20, y=140, width=40, height=40)
button_8.place(x=80, y=140, width=40, height=40)
button_9.place(x=140, y=140, width=40, height=40)
button_divide.place(x=200, y=140, width=40, height=40)

button_4.place(x=20, y=200, width=40, height=40)
button_5.place(x=80, y=200, width=40, height=40)
button_6.place(x=140, y=200, width=40, height=40)
button_multiply.place(x=200, y=200, width=40, height=40)

button_1.place(x=20, y=260, width=40, height=40)
button_2.place(x=80, y=260, width=40, height=40)
button_3.place(x=140, y=260, width=40, height=40)
button_minus.place(x=200, y=260, width=40, height=40)

button_0.place(x=20, y=320, width=100, height=40)
button_point.place(x=140, y=320, width=40, height=40)
button_plus.place(x=200, y=320, width=40, height=40)

root.mainloop()