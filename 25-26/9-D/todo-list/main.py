import tkinter as tk
import json

TODO_LIST_FILE = "25-26/9-D/todo-list/todo-list.json"

todos = []



try:
    with open(TODO_LIST_FILE, "r") as file:
        todos = json.load(file)
except:
    with open(TODO_LIST_FILE, "w") as file:
        todos = json.dump(file)



def add_new_task():
    global todos

    todos.insert(0, input_entry.get())

    with open(TODO_LIST_FILE, "w", encoding="utf-8") as file:
        todos = json.dump(file)

    input_entry.delete(0, "end")



root = tk.Tk()
root.title("Список завдань")
root.geometry("600x650")
root.resizable(False, False)

input_label = tk.Label(root, text="Введіть нове завдання:", font="Arial 14 bold")
input_entry = tk.Entry(root, font="Arial 14 bold", width=50)
add_task_button = tk.Button(root, text="Додати завдання", command=add_new_task)

input_label.place(x=20, y=20)
input_entry.place(x=20, y=50)
add_task_button.place(relx=0.5, y=100, anchor="center")

root.mainloop()