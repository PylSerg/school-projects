text = "Розділення тексту та об'єднання елементів списку у Python"

# .split("separator") - розділяє рядок на список елементів
text_list = text.split(" ")

# "separator".join() - об'єднує елементи списку в рядок
new_text_1 = "-".join(text_list).lower()
new_text_2 = "_".join(text_list).upper()

print(f"\n{new_text_1}")
print(f"\n{new_text_2}")
