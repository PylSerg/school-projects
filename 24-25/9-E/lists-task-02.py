# 2. Список оцінок:

# Створіть список з 10 випадкових оцінок (від 1 до 12).
# Виведіть список на екран.
# Знайдіть середнє арифметичне оцінок.
# Знайдіть максимальну та мінімальну оцінки.
# Виведіть результати на екран.

# sum() - обчислює суму всіх елементів списку
# len() - повертає кількість елементів у списку
# max() - повертає максимальний елемент списку
# min() - повертає мінімальний елемент списку

from random import randint

grades = [randint(1, 12) for _ in range(10)]

# for _ in range(10):
#     grades.append(randint(1, 12))

print(f"\n\nСписок оцінок: {grades}")

average_grade = sum(grades) / len(grades)
print(f"\nСередня оцінка: {average_grade}")

max_grade = max(grades)
min_grade = min(grades)
print(f"Максимальна оцінка: {max_grade}")
print(f"Мінімальна оцінка: {min_grade}")