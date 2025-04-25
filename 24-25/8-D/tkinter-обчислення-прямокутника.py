# justify - вирівнювання тексту по ширині ("left", "right", "center")
# wraplength - максимальна ширина тексту в пікселях, після якої текст буде перенесено на новий рядок

from tkinter import Tk, Label, Button, Entry, messagebox

# Функція для обчислення площі та периметра прямокутника
def calc():
    # Отримання значень сторін A та B з полів вводу
    a = side_a_entry.get()
    b = side_b_entry.get()
    
    # Перевіряємо введені дані.
    # Якщо хоча б одне із полів порожнє - показуємо вікно з помилкою, та виходимо із функції
    if a == "" or b == "":
        messagebox.showerror(title="Error", message="Сторони А і В не можуть бути порожніми!")
        return
    
    # Перетворення значень у тип float  
    a = float(a)
    b = float(b)
        
    # Перевіряємо введені дані.
    # Якщо хоча б одне значення менше або дорівнює 0 - показуємо вікно з помилкою, та виходимо із функції
    if a <= 0 or b <= 0:
        messagebox.showerror(title="Error", message="Сторони А і В не можуть бути від'ємними або дорівнювати 0!")
        return
    
    # обчислення площі та периметра
    area = a * b
    perimeter = 2 * (a + b)
    
    # Виведення результатів у текстові написи
    area_label["text"] = f"Площа прямокутника зі сторонами {a} од. та {b} од. дорівнює {area} од.²"
    perimeter_label["text"] = f"Периметр прямокутника зі сторонами {a} од. та {b} од. дорівнює {perimeter} од."
    
    # Очищення полів вводу
    side_a_entry.delete(0, 'end')
    side_b_entry.delete(0, 'end')

# Створення основного вікна програми
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
calc_button = Button(root, text="Обчислити", width=15, height=2, command=calc)

# Створення текстового напису для результату
result_label = Label(root, text="РЕЗУЛЬТАТ:", font=("Arial", 14, "bold"))
area_label = Label(root, font=("Arial", 12), justify="left", wraplength=350)
perimeter_label = Label(root, font=("Arial", 12), justify="left", wraplength=350)



# Розміщення віджетів
side_a_label.place(x=20, y=20)
side_a_entry.place(x=100, y=22)
side_b_label.place(x=20, y=50)
side_b_entry.place(x=100, y=52)
calc_button.place(x=250, y=25)

result_label.place(x=20, y=150)
area_label.place(x=20, y=200)
perimeter_label.place(x=20, y=250)



root.mainloop()