# Камінь ламає ножиці
# Ножиці ріжуть папір
# Папір накриває камінь

from random import randint

print("\n\n========== КАМІНЬ - НОЖИЦІ - ПАПІР ==========\n\n")
print("Камінь ламає ножиці \nНожиці ріжуть папір \nПапір накриває камінь")

count_comp = 0
count_player = 0

while True:
    comp = randint(0, 2)
    player = input("\n\nВаш вибір (к/н/п/х): ")

    if player == "х": exit()

    if comp == 0:
        comp = "Камінь"
    elif comp == 1:
        comp = "Ножиці"
    elif comp == 2:
        comp = "Папір"

    if player == "к":
        player = "Камінь"
    elif player == "н":
        player = "Ножиці"
    elif player == "п":
        player = "Папір"
    else:
        print("ПОМИЛКА: Неправильний вибір!")

    print()
    print(f"Комп'ютер вибрав: {comp}")
    print(f"Ви вибрали: {player}")

    # Ящо комп'ютер вибрав камінь
    if comp == "Камінь":
        if player == "Камінь":
            print("Нічия!")
        elif player == "Ножиці":
            print("Ви програли!")
            count_comp += 1
        elif player == "Папір":
            print("Ви виграли!")
            count_player += 1
    # Ящо комп'ютер вибрав ножиці
    elif comp == "Ножиці":
        if player == "Камінь":
            print("Ви виграли!")
            count_player += 1
        elif player == "Ножиці":
            print("Нічия!")
        elif player == "Папір":
            print("Ви програли!")
            count_comp += 1
    # Ящо комп'ютер вибрав папір
    elif comp == "Папір":
        if player == "Камінь":
            print("Ви програли!")
            count_comp += 1
        elif player == "Ножиці":
            print("Ви виграли!")
            count_player += 1
        elif player == "Папір":
            print("Нічия!")

    # Підрахунок очок
    print(f"\n\nРахунок: \nКомп'ютер {count_comp} : {count_player} Ви")
