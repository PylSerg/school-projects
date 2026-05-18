import tkinter as tk
import json

TODO_LIST_FILE = "25-26/9-D/todo-list/todo-list.json"

todos = []



try:
    with open(TODO_LIST_FILE, "r") as file:
        todos = json.load(file)
except:
    with open(TODO_LIST_FILE, "w") as file:
        json.dump(todos, file)


def update_todos_list():
    global todos_frame

    todos_frame.destroy()

    todos_frame = tk.Frame(root, width=500, height=500)
    todos_frame.place(x=20, y=180)

    for indx, todo in enumerate(todos, start=1):
        position_y = indx * 40

        task_label = tk.Label(todos_frame, text=f"{indx}. {todo}", font="Arial 14", justify="left")
        task_label.place(x=40, y=position_y)

        delete_button = tk.Button(todos_frame, text="X", font="Arial 12 bold", fg="red", command=lambda j=indx-1: delete_task(j))
        delete_button.place(x=20, y=position_y)



def add_new_task():
    todos.insert(0, input_entry.get())

    with open(TODO_LIST_FILE, "w") as file:
        json.dump(todos, file)

    input_entry.delete(0, "end")
    
    update_todos_list()

def delete_task(task_number):
    todos.pop(task_number)

    with open(TODO_LIST_FILE, "w") as file:
        json.dump(todos, file)

    update_todos_list()



root = tk.Tk()
root.title("Список завдань")
root.geometry("600x650")
root.resizable(False, False)

input_label = tk.Label(root, text="Введіть нове завдання:", font="Arial 14 bold")
input_entry = tk.Entry(root, font="Arial 14 bold", width=50)
add_task_button = tk.Button(root, text="Додати завдання", command=add_new_task)

todos_label = tk.Label(root, text="Список завдань", font="Arial 14 bold")
todos_frame = tk.Frame(root)


input_label.place(x=20, y=20)
input_entry.place(x=20, y=50)
add_task_button.place(relx=0.5, y=100, anchor="center")
todos_label.place(x=20, y=150)

update_todos_list()

root.mainloop()