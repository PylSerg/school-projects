from tkinter import Tk, Label, Entry, Button, Frame
import json

todos_list = "todos-list.json"
todos = []

try:
    with open(todos_list, "r") as file:
        todos = json.load(file)
except:
    with open(todos_list, "w") as file:
        json.dump(todos, file)
        

def add_new_task():
    todos.append(input_entry.get())

    with open(todos_list, "w") as file:
        json.dump(todos, file)
        
    input_entry.delete(0, "end")
   
    
def delete_task(task_number):
    todos.pop(task_number - 1)

    with open(todos_list, "w") as file:
        json.dump(todos, file)



root = Tk()
root.title("TODOS")
root.geometry("600x600")

input_label = Label(root, text="Введіть нове завдання:", font=("Arial", 14, "bold"))
input_label.place(x=20, y=20)

input_entry = Entry(root, font=("Arial", 14, "normal"), width=50)
input_entry.place(x=20, y=50)

add_task_button = Button(root, text="Додати завдання", font=("Arial", 12, "normal"))
add_task_button.place(relx=0.5, y=100, anchor="center")

todos_list = Label(root, text="Список завдань:", font=("Arial", 14, "bold"))
todos_list.place(x=20, y=150)

todos_frame = Frame(root)

root.mainloop() 