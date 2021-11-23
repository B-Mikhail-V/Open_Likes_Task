import os
from pprint import pprint

# print(os.getcwd())
path = os.path.join(os.getcwd(), 'recipes.txt')
# print(path)

with open(path, encoding='utf-8') as dishes:
    result = {}
    for dish in dishes:
        dish_name = dish.strip()
        counter = int(dishes.readline().strip())
        temp_list = []
        for ingredient in range(counter):
            ingredient_name, ingredient_quantity, ingredient_measure = dishes.readline().split("|")
            # print (ingredient_name, ingredient_quantity, ingredient_measure)
            temp_list.append({'ingredient_name': ingredient_name.strip(), 'quantity':  ingredient_quantity.strip(),
                              'measure': ingredient_measure.strip()})
        result[dish_name] = temp_list
        dishes.readline()
    # pprint(result)
dish_order = ['Омлет', 'Утка по-пекински']
qty_order = 4
for key, value in result.items():
    if key in dish_order:
        print(key)
        for item in value:
            # print(item)
            # print(qty_order)
            qty_ing = int(item['quantity']) * qty_order
            print(item['ingredient_name'], qty_ing, item['measure'])

