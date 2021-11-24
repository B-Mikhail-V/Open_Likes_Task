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

def get_shop_list_by_dishes(dishes, person_count):
    dishes_total = dishes * person_count
    ingredient_order_list = []
    for key, value in result.items():
        if key in dishes_total:
            ing_dict = {}
            for ingredient in value:
                # print(ingredient['ingredient_name'])
                ingredient_quantity_order = ingredient['quantity']
                # print(ingredient['ingredient_name'], ingredient_quantity_order, ingredient['measure'])
                list_temp = [ingredient['ingredient_name'],]
                ing_dict[ingredient['ingredient_name']] = [{'quantity':  ingredient['quantity'], 'measure':  ingredient['measure']}]
            pprint(ing_dict)

print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2))