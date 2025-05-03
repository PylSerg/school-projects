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



def update_todos_list():
    global todos_frame
    todos_frame.destroy()
    
    todos_frame = Frame(root, width=500, height=500)
    todos_frame.place(x=20, y=180)
    
    for i, todo in enumerate(todos, start=1):
        position_y = i * 40
        
        task_label = Label(todos_frame, text=f"{i}. {todo}", font=("Arial", 14), justify="left")
        task_label.place(x=60, y=position_y)
        
        delete_button = Button(todos_frame, text="X", font=("Arial", 12, "bold"), fg="red", command=lambda j=i: delete_task(j))
        delete_button.place(x=20, y=position_y)
        

        
def add_new_task():
    todos.append(input_entry.get())    
    
    with open(todos_list, "w") as file:
        json.dump(todos, file)
    
    input_entry.delete(0, "end")
    
    update_todos_list()



def delete_task(task_number):
    todos.pop(task_number - 1)
    
    with open(todos_list, "w") as file:
        json.dump(todos, file)
    
    update_todos_list()


root = Tk()
root.title("TODOS")
root.geometry("600x600")

input_label = Label(root, text="Введіть нове завдання:", font=("Arial", 14, "bold"))
input_label.place(x=20, y=20)

input_entry = Entry(root, font=("Arial", 14), width="50")
input_entry.place(x=20, y=50)

add_task_button = Button(root, text="Додати завдання", command=add_new_task)
add_task_button.place(relx=0.5, y=100, anchor="center")

todos_label = Label(root, text="Список завдань:", font=("Arial", 14, "bold"))
todos_label.place(x=20, y=150)
    
todos_frame = Frame(root)

update_todos_list()

root.mainloop()