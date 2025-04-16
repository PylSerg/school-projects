from tkinter import Tk, Label, Button, Entry

# Label - це текстовий віджет, який відображає текст на вікні
# Button - це кнопка, на яку можна натискати
# Entry - це текстове поле, в яке можна вводити текст

def on_button_click():
    name = name_entry.get()  # отримуємо текст з текстового поля
    text_label["text"] = f"Привіт, {name}!"  # змінюємо текст в текстовому віджеті
    text_label.place(relx=0.5, rely=0.5, anchor="center")  # розміщуємо текстовий віджет по центру
    
    name_entry.destroy()  # видаляємо текстове поле
    button.destroy()  # видаляємо кнопку


root = Tk()  # створюємо основне вікно програми
root.title("My First GUI")  # задаємо заголовок вікна
root.geometry("200x150")  # задаємо розміри вікна

text_label = Label(root, text="Введіть ваше ім'я:")  # створюємо текстовий віджет
name_entry = Entry(root)  # створюємо текстове поле для вводу
button = Button(root, text="OK", command=on_button_click)  # створюємо кнопку з текстом "OK"

text_label.pack(pady=20)  # додаємо текстовий віджет до вікна
name_entry.pack() # додаємо текстове поле до вікна
button.pack(pady=20)  # додаємо кнопку до вікна

root.mainloop()  # запускаємо основний цикл програми