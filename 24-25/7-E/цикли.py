# from time import sleep - імпортує функцію sleep з модуля time, яка дозволяє затримувати виконання програми на певний час.
# while count > 0: - цикл, який виконується, поки значення count більше 0.
# count -= 1 - зменшує значення count на 1 в кожній ітерації циклу.
# print(count) - виводить значення count на кожній ітерації циклу.
# sleep(1) - затримує виконання програми на 1 секунду.



from time import sleep

count = 30

print(f"\n\nЗапуск таймера на {count} секунд\n")

while count > 0:
    count -= 1

    print(count)

    sleep(1)

print("\nЧас вийшов!\n")