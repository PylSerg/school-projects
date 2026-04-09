from tkinter import *


# Функція автоматичного розрахунку вартості
# *arg - приймаємо усі аргументи, так як не знаємо 
# скільки їх передасться при певному виклику функції

def calc_cost(*args):
    cost_1["text"] = int(price_1.get() or 0) * scale_1.get()
    cost_2["text"] = int(price_2.get() or 0) * scale_2.get()
    cost_3["text"] = int(price_3.get() or 0) * scale_3.get()
    cost_4["text"] = int(price_4.get() or 0) * scale_4.get()
    
    total_cost_sum["text"] = f"{cost_1["text"] + cost_2["text"] + cost_3["text"] + cost_4["text"]} грн."


# Створюємо головне вікно
root = Tk()
root.title("Замовлення")
root.geometry("440x300")


# Створюємо віджети
header_1 = Label(root, text="Найменування", font="Arial 10 bold")
header_2 = Label(root, text="Ціна, грн", font="Arial 10 bold")
header_3 = Label(root, text="Кількість", font="Arial 10 bold")
header_4 = Label(root, text="Вартість, грн", font="Arial 10 bold")

name_1 = Label(root, text="Піца", font="Arial 10 normal")
name_2 = Label(root, text="Морозиво", font="Arial 10 normal")
name_3 = Label(root, text="Тістечко", font="Arial 10 normal")
name_4 = Label(root, text="Сік", font="Arial 10 normal")

# Створюємо контрольну змінну StringVar(), 
# та прив'язуємо до неї віджет Entry за допомогою параметра textvariable.
# Відслідковуємо контрольну змінну за допомогою trace_add(), 
# і у разі зміни ціни викликаємо функцію calc_cost.

p1 = StringVar()
price_1 = Entry(root, font="Arial 12 normal", bg="sky blue", justify="center", textvariable=p1)
price_1.insert(END, "75")
p1.trace_add("write", calc_cost)

p2 = StringVar()
price_2 = Entry(root, font="Arial 12 normal", bg="sky blue", justify="center", textvariable=p2)
price_2.insert(END, "12")
p2.trace_add("write", calc_cost)

p3 = StringVar()
price_3 = Entry(root, font="Arial 12 normal", bg="sky blue", justify="center", textvariable=p3)
price_3.insert(END, "16")
p3.trace_add("write", calc_cost)

p4 = StringVar()
price_4 = Entry(root, font="Arial 12 normal", bg="sky blue", justify="center", textvariable=p4)
price_4.insert(END, "8")
p4.trace_add("write", calc_cost)

scale_1 = Scale(root, orient=HORIZONTAL, length=50, from_=0, to=10, command=calc_cost)
scale_2 = Scale(root, orient=HORIZONTAL, length=50, from_=0, to=10, command=calc_cost)
scale_3 = Scale(root, orient=HORIZONTAL, length=50, from_=0, to=10, command=calc_cost)
scale_4 = Scale(root, orient=HORIZONTAL, length=50, from_=0, to=10, command=calc_cost)

cost_1 = Label(root, text=0, font="Arial 12 normal", bg="deep sky blue")
cost_2 = Label(root, text=0, font="Arial 12 normal", bg="deep sky blue")
cost_3 = Label(root, text=0, font="Arial 12 normal", bg="deep sky blue")
cost_4 = Label(root, text=0, font="Arial 12 normal", bg="deep sky blue")

total_cost_title = Label(root, text="Вартість замовлення:", font="Arial 12 normal")
total_cost_sum = Label(root, text="0 грн", font="Arial 12 bold")



# Розміщуємо віджети
header_1.place(x=20, y=20)
header_2.place(x=150, y=20)
header_3.place(x=230, y=20)
header_4.place(x=310, y=20)

name_1.place(x=20, y=60)
price_1.place(x=150, y=60, width=60, height=30)
scale_1.place(x=230, y=50)
cost_1.place(x=310, y=60, width=60, height=30)

name_2.place(x=20, y=100)
price_2.place(x=150, y=100, width=60, height=30)
scale_2.place(x=230, y=90)
cost_2.place(x=310, y=100, width=60, height=30)

name_3.place(x=20, y=140)
price_3.place(x=150, y=140, width=60, height=30)
scale_3.place(x=230, y=130)
cost_3.place(x=310, y=140, width=60, height=30)

name_4.place(x=20, y=180)
price_4.place(x=150, y=180, width=60, height=30)
scale_4.place(x=230, y=170)
cost_4.place(x=310, y=180, width=60, height=30)

total_cost_title.place(x=20, y=250)
total_cost_sum.place(x=200, y=250)


root.mainloop()