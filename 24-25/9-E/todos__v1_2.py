from tkinter import Tk, Label, Entry, Button, Frame
import json

todos_list = "todos-list.json"
todos = []

part = 10


try:
    with open(todos_list, "r") as file:
        todos = json.load(file)
except:
    with open(todos_list, "w") as file:
        json.dump(todos, file)



def update_todos_list():
    global todos_frame
    todos_frame.destroy()
    
    todos_frame = Frame(root, width=500, height=450)
    todos_frame.place(x=20, y=180)
    
    position_y = 40
    
    for i, todo in enumerate(todos, start=1):
        if i > (part - 10) and i <= part:
            task_label = Label(todos_frame, text=f"{i}. {todo}", font=("Arial", 14), justify="left")
            task_label.place(x=60, y=position_y)
            
            delete_button = Button(todos_frame, text="X", font=("Arial", 12, "bold"), fg="red", command=lambda j=i: delete_task(j))
            delete_button.place(x=20, y=position_y)
            
            previous_position_button = Button(todos_frame, text="▲", command=lambda j=i-1: previous_position(j))
            previous_position_button.place(x=440, y=position_y)
            
            next_position_button = Button(todos_frame, text="▼", command=lambda j=i-1: next_position(j))
            next_position_button.place(x=470, y=position_y)
            
            position_y += 40
        

        
def add_new_task():
    todos.insert(0, input_entry.get())    
    
    with open(todos_list, "w") as file:
        json.dump(todos, file)
    
    input_entry.delete(0, "end")
    
    update_todos_list()


def delete_task(task_number):
    todos.pop(task_number - 1)
    
    with open(todos_list, "w") as file:
        json.dump(todos, file)
    
    update_todos_list()
    

def previous_position(task_index):
    todos.insert(task_index - 1, todos.pop(task_index))
    
    with open(todos_list, "w") as file:
        json.dump(todos, file)
    
    update_todos_list()
    

def next_position(task_index):
    todos.insert(task_index + 1, todos.pop(task_index))
    
    with open(todos_list, "w") as file:
        json.dump(todos, file)
    
    update_todos_list()


def previous_page():
   global part
   
   if part == 10: return 
   
   part -= 10
   
   update_todos_list()
   

def next_page():
    global part
    
    part += 10
    
    if (part - len(todos)) > 10: part -= 10
    
    update_todos_list()


root = Tk()
root.title("TODOS")
root.geometry("600x650")
root.resizable(False, False)

input_label = Label(root, text="Введіть нове завдання:", font=("Arial", 14, "bold"))
input_label.place(x=20, y=20)

input_entry = Entry(root, font=("Arial", 14), width="50")
input_entry.place(x=20, y=50)

add_task_button = Button(root, text="Додати завдання", command=add_new_task)
add_task_button.place(relx=0.5, y=100, anchor="center")

sort_label = Label(root, text="Сортування:", font=("Arial", 12, "bold"))
sort_label.place(x=360, y=130)

todos_label = Label(root, text=f"Список завдань ({len(todos)})", font=("Arial", 14, "bold"))
todos_label.place(x=20, y=150)
    
todos_frame = Frame(root)

previous_button = Button(root, text="▲", height=10, command=previous_page)
previous_button.place(x=550, y=250)

next_button = Button(root, text="▼", height=10, command=next_page)
next_button.place(x=550, y=430)

update_todos_list()

root.mainloop()