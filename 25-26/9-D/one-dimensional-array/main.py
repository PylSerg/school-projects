# list() — створення списку
# map() — перетворення елементів у список
# input() — отримання даних з рядка
# int — перетворення на цілі числа
# split() — розділення рядка на елементи

numbers = list(map(int, input("Enter numbers: ").split()))
result = 0

for number in numbers:
    result += number

print(f"\n\nResult: {result}")
