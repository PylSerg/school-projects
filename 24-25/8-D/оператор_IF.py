action = input("Виберіть дію (s/p): ")

if (action != "s" and action != "p"):
    print("Помилка: Введіть s або p!")
    exit()

a = float(input("Введіть сторону А: "))
b = float(input("Введіть сторону B: "))

if (action == "s"):
    s = a * b
    print(f"Площа прямокутника зі сторонами {a} та {b} дорівнює {s} од²")
    
if (action == "p"):
    p = 2 * (a + b)
    print(f"Периметр прямокутника зі сторонами {a} та {b} дорівнює {p} од")
    
input("\n\n*** Press ENTER to exit ***")