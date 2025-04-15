# Камінь ламає ножиці
# Ножиці ріжуть папір
# Папір накриває камінь

from random import randint 
choice=["камінь", "ножиці", "папір"]

print ("Почнемо гру Камінь - ножиці - папір")
for i in range(3):
    print (i, choice[i])

game="y" 
while game=="y": 
    comp=randint(0,2)
    player=int(input("Оберіть 0, 1 або 2 ")) 
    player_choice=choice[player] 
    comp_choice=choice[comp] 
    print ()
    print ("Комп'ютер вибрав ", comp_choice)
    print ("Ваш вибір ", player_choice)
  
    # Якщо комп'ютер вибрав КАМІНЬ 
    if comp==0: 
        if player==0:
            print ("НІЧИЯ")
        if player==1:
            print ("Виграв комп'ютер") 
        if player==2:
            print ("Ви перемогли!")

    # Якщо комп'ютер вибрав НОЖИЦІ 
    if comp==1: 
        if player==1:
            print ("НІЧИЯ")
        if player==2:
            print ("Виграв комп'ютер") 
        if player==0:
            print ("Ви перемогли!")

    # Якщо комп'ютер вибрав ПАПІР 
    if comp==2: 
        if player==2:
            print ("НІЧИЯ")
        if player==0:
            print ("Виграв комп'ютер") 
        if player==1:
            print ("Ви перемогли!") 

    print ()
    game=input("Бажаєте продовжити? (y/n)") 

print ("Дякую за гру!")
