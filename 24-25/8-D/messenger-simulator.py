from datetime import datetime
from time import sleep

counter = 0

def show_message(user="Помилка", text="Неправильний формат повідомлення!"):
    global counter
    
    sleep(5)
    
    counter += 1
    print(f"Нових повідомлень: {counter}")
    
    today = datetime.today()
    print(today.strftime(f"\n[%d-%m-%Y %H:%M:%S]\n"))
    
    print(f"{user}: {text}")
    print("\n\n\n")
    


show_message("Стів", "Привіт!")
show_message("Джон", "Привіт!")
show_message("Джон", "Як твої справи?")
show_message()