from tkinter import *


# Оголошення змінних
bfs = "Arial 14 bold"

action = ""
result = ""
a = ""
b = ""


# Очищення поля введення
def clear_input():
    global a, b, result, action
    
    if entry.get() == "" or result != "":
        action = ""
        result = ""
        a = ""
        b = ""
        label_memory["text"] = ""
        entry.delete(0, END)
    else:
        entry.delete(0, END)
        

# Додає мінус до числа
def toggle_minus():
    if entry.get() and entry.get()[0] == "-":
        entry.delete(0, 1)
    else:
        entry.insert(0, "-")


# Вибір дії
def select_action(act):
    global a, action

    action = act
    a = entry.get()
    entry.delete(0, END)
    
    label_memory["text"] = f"{a} {action}"
    
    
# Калькуляція
def calc():
    global a, b, result
    
    b = entry.get()
    entry.delete(0, END)
    
    if b[0] == "-":
        label_memory["text"] = f"{a} {action} ({b}) ="
    else:
        label_memory["text"] = f"{a} {action} {b} ="

    a = float(a)
    b = float(b)
    
    if action == "÷" : result = a / b
    if action == "×" : result = a * b
    if action == "-" : result = a - b
    if action == "+" : result = a + b
    
    entry.insert(END, result)
    

# Створення головного вікна
root = Tk()
root.title("Калькулятор")
root.geometry("260x410")
root.resizable(False, False)


# Створення віджетів
label_memory = Label(root, text="", font="Arial 10 normal", anchor="e", fg="grey")
entry = Entry(root, font="Arial 14 normal", justify="right")

button_c = Button(root, text="C", font=bfs, command=clear_input)
button_d = Button(root, text="←", font=bfs, command=lambda: entry.delete(len(entry.get())-1, END))
button_equal = Button(root, text="=", font=bfs, command=calc)

button_divide = Button(root, text="÷", font=bfs, command=lambda: select_action("÷"))
button_multiply = Button(root, text="×", font=bfs, command=lambda: select_action("×"))
button_minus = Button(root, text="-", font=bfs, command=lambda: select_action("-"))
button_plus = Button(root, text="+", font=bfs, command=lambda: select_action("+"))

button_point = Button(root, text=".", font=bfs, command=lambda: entry.insert(END, "."))
button_toggle_minus = Button(root, text="±", font=bfs, command=toggle_minus)

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
label_memory.place(x=20, y=20, width=220, height=20)
entry.place(x=20, y=50, width=220, height=40)

button_c.place(x=20, y=110, width=40, height=40)
button_d.place(x=80, y=110, width=40, height=40)
button_equal.place(x=140, y=110, width=100, height=40)

button_7.place(x=20, y=170, width=40, height=40)
button_8.place(x=80, y=170, width=40, height=40)
button_9.place(x=140, y=170, width=40, height=40)
button_divide.place(x=200, y=170, width=40, height=40)

button_4.place(x=20, y=230, width=40, height=40)
button_5.place(x=80, y=230, width=40, height=40)
button_6.place(x=140, y=230, width=40, height=40)
button_multiply.place(x=200, y=230, width=40, height=40)

button_1.place(x=20, y=290, width=40, height=40)
button_2.place(x=80, y=290, width=40, height=40)
button_3.place(x=140, y=290, width=40, height=40)
button_minus.place(x=200, y=290, width=40, height=40)

button_0.place(x=20, y=350, width=40, height=40)
button_point.place(x=80, y=350, width=40, height=40)
button_toggle_minus.place(x=140, y=350, width=40, height=40)
button_plus.place(x=200, y=350, width=40, height=40)

root.mainloop()
