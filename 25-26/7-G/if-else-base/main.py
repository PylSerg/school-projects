# 1. Ввід даних

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))


# 2. Обчислення і вивід

if a > b:
    print(f"\n a = {a}")
elif b > a:
    print(f"\n b = {b}")
else:
    print(f"\n a = b = {a}")