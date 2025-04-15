from random import randrange

print("Гра: Вгадай число\n\n")

min = -100
max = 100

x = randrange(min, max)

counter = 1

print(f"Я загадав число від {min} до {max}. Спробуй його вгадати.\n\n")

while True:
    user_number = int(input(f"{counter} спроба: "))
    
    if user_number == x :
        print(f"Вітаю! Я дійсно загадав число {x}!\n")
        break
    
    if user_number < x :
        print(f"Моє число більше ніж {user_number}\n")
        counter += 1
        
    if user_number > x :
        print(f"Моє число менше ніж {user_number}\n")
        counter += 1