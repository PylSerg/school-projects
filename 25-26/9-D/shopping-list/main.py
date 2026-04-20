shopping_list = []

while True:
    new_item = input("\nДодати продукт до списку: ")

    if new_item == "" : break

    shopping_list.append(new_item)


print("\nСписок продуктів:")

for i in range(len(shopping_list)):
    print(f"{i + 1}. {shopping_list[i]}")