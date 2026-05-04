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