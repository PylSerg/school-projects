from tkinter import *

root = Tk()
root.title("Замовлення")
root.geometry("440x300")

# Створення віджетів
h1 = Label(root, text="Найменування", font="Arial 10 bold")
h2 = Label(root, text="Ціна, грн", font="Arial 10 bold")
h3 = Label(root, text="Кількість", font="Arial 10 bold")
h4 = Label(root, text="Вартість, грн", font="Arial 10 bold")

n1 = Label(root, text="Піца", font="Arial 10 normal")
n2 = Label(root, text="Морозиво", font="Arial 10 normal")
n3 = Label(root, text="Тістечко", font="Arial 10 normal")
n4 = Label(root, text="Сік", font="Arial 10 normal")

p1 = Entry(root, font="Arial 12 normal", bg="sky blue", justify="center")
p1.insert(END, "75")
p2 = Entry(root, font="Arial 12 normal", bg="sky blue", justify="center")
p2.insert(END, "12")
p3 = Entry(root, font="Arial 12 normal", bg="sky blue", justify="center")
p3.insert(END, "16")
p4 = Entry(root, font="Arial 12 normal", bg="sky blue", justify="center")
p4.insert(END, "8")


# Розміщення віджетів
h1.place(x=20, y=20)
h2.place(x=150, y=20)
h3.place(x=230, y=20)
h4.place(x=310, y=20)

n1.place(x=20, y=60)
p1.place(x=150, y=60, width=60, height=30)

n2.place(x=20, y=100)
p2.place(x=150, y=100, width=60, height=30)

n3.place(x=20, y=140)
p3.place(x=150, y=140, width=60, height=30)

n4.place(x=20, y=180)
p4.place(x=150, y=180, width=60, height=30)

root.mainloop()