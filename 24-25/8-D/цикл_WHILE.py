def calculate(action):
    while True:
        a = float(input("Введіть сторону А: "))
        
        if a > 0: break
        
        print("Значення повинно бути більшим за 0!")
        
    while True:
        b = float(input("Введіть сторону B: "))
        
        if b > 0: break
            
        print("Значення повинно бути більшим за 0!")

    if (action == "s"):
        s = a * b
        print(f"Площа прямокутника зі сторонами {a} та {b} дорівнює {s} од² \n\n\n")

    if (action == "p"):
        p = 2 * (a + b)
        print(f"Периметр прямокутника зі сторонами {a} та {b} дорівнює {p} од \n\n\n")
    
while True:
    action = input("Виберіть дію (s/p): ")

    if (action == ""):
        break       
    if (action == "s" or action == "p"):
        calculate(action)
    else:
        print("Помилка: Введіть s або p!")
        