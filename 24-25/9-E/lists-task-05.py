## 5. Список завдань: Видалити завдання зі списку

import json

todos_list = "todos-list.json" # Ім'я файлу для зберігання списку завдань
todos = [] # Ініціалізація списку завдань

# Перевірка наявності файлу та його створення, якщо він не існує
try:
    with open(todos_list, "r") as file:
        todos = json.load(file) # Завантаження списку завдань з файлу
except:
    with open(todos_list, "w") as file:
        json.dump(todos, file) # Створення нового файлу, якщо він не існує

while True:
    print("\n"+"="*50)
    print("\nСписок завдань:")

    # Виведення списку завдань
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo}")
        
    print("\n"+"="*50)
    
    # Виведення варіантів дій
    print("\n\nВиберіть дію:")
    print("1. Додати завдання")
    print("2. Видалити завдання")
    print("3. Вихід з програми")
    
    action = input("\nВибір: ") # Отримання вибору дії від користувача
    
    # Перевірка вибору та виконання відповідної дії
    if action == "1":
        task = input("\nВведіть завдання: ") # Отримання нового завдання від користувача
    
        todos.append(task) # Додавання нового завдання до списку

        with open(todos_list, "w") as file:
            json.dump(todos, file) # Збереження оновленого списку завдань у файл
    elif action == "2":
        task_number = int(input("\nВведіть номер завдання для видалення: "))

        # Перевірка, чи номер завдання дійсний
        # Якщо так, видалити його зі списку
        if 1 <= task_number <= len(todos):
            todos.pop(task_number - 1) # Видалення завдання за номером

            with open(todos_list, "w") as file:
                json.dump(todos, file) # Збереження оновленого списку завдань у файл
        else:
            print("Неправильний номер завдання.")
    elif action == "3":
        exit() # Вихід з програми
    else:
        print("Неправильний вибір. Спробуйте ще раз.")    