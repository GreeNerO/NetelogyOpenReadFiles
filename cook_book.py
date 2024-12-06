from pprint import pprint 

cook_book = {}

with open('recipes/recipes.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

    i = 0
    while i < len(lines):
        if not lines[i].strip():  # Пропускаем пустые строки
            i += 1
            continue

        dish_name = lines[i]  # Название блюда
        ingredient_count = int(lines[i + 1])  # Количество ингредиентов
        ingredients = []

        for j in range(i + 2, i + 2 + ingredient_count):
            parts = lines[j].split('|')  # Разбиваем строку вручную
            ingredient_name = parts[0].strip()
            quantity = int(parts[1].strip())
            measure = parts[2].strip()

            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })

        cook_book[dish_name] = ingredients
        i += 2 + ingredient_count  # Переход к следующему рецепту

pprint(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:  # Проверяем, есть ли блюдо в cook_book
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name in shop_list:
                    # Если ингредиент уже есть в списке, увеличиваем количество
                    shop_list[name]['quantity'] += quantity
                else:
                    # Если ингредиента нет, добавляем его
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' отсутствует в cook_book.")  # Сообщение о пропущенном блюде

    return shop_list


result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(result)
