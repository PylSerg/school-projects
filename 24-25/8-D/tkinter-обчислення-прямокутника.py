from tkinter import Tk, Label, Button, Entry

root = Tk()
root.title("Обчислення прямокутника")
root.geometry("400x400")

# Створення текстового напису та поля вводу для сторони A
side_a_label = Label(root, text="Сторона A:")
side_a_entry = Entry(root)

# Створення текстового напису та поля вводу для сторони B
side_b_label = Label(root, text="Сторона B:")
side_b_entry = Entry(root)

# Створення кнопки для обчислення
calc_button = Button(root, text="Обчислити", width=15, height=2)

# Створення текстового напису для результату
result_label = Label(root, text="РЕЗУЛЬТАТ:", font=("Arial", 14, "bold"))
area_label = Label(root)
perimeter_label = Label(root)



# Розміщення віджетів
side_a_label.place(x=20, y=20)
side_a_entry.place(x=100, y=22)
side_b_label.place(x=20, y=50)
side_b_entry.place(x=100, y=52)
calc_button.place(x=250, y=25)



root.mainloop()