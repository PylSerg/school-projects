from tkinter import *


def calc_pl():
    a = float(input_a.get())
    b = float(input_b.get())
    
    if (a > 0 and b > 0):
        result_text["text"] = f"Площа прямокутника {a * b} од²."
    else:
        result_text["text"] = "Сторона повинна бути більшою за 0."

def calc_pr():
    a = float(input_a.get())
    b = float(input_b.get())
    
    if (a > 0 and b > 0):
        result_text["text"] = f"Периметр прямокутника {2 * (a + b)} од."
    else:
        result_text["text"] = "Сторона повинна бути більшою за 0."
    
    
    
root = Tk()
root.title("Калькулятор площі та периметру")
root.geometry("600x400")

label_a = Label(root, text="Сторона A: ", font="Arial 14 normal")
label_b = Label(root, text="Сторона B: ", font="Arial 14 normal")

input_a = Entry(root, font="Arial 14 normal")
input_b = Entry(root, font="Arial 14 normal")

button_pl = Button(root, text="Обрахувати площу", font="Arial 14 normal", command=calc_pl)
button_pr = Button(root, text="Обрахувати периметр", font="Arial 14 normal", command=calc_pr)

result_title = Label(root, text="РЕЗУЛЬТАТ:", font="Arial 18 bold")
result_text = Label(root, text="", font="Arial 14 normal")

label_a.place(x=10, y=10)
input_a.place(x=130, y=10)
label_b.place(x=10, y=50)
input_b.place(x=130, y=50)
button_pl.place(x=10, y=100)
button_pr.place(x=200, y=100)
result_title.place(x=30, y=200)
result_text.place(x=30, y=250)

root.mainloop()