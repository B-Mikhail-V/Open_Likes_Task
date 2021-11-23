import os

print(os.getcwd())
path = os.path.join(os.getcwd(), 'recipes.txt')
print(path)

with open(path, encoding='utf-8') as dishes:
    result = {}
    for dish in dishes:
        dish_name = dish
        print(dish)
        counter = int(dishes.readline().strip())
        for igredient in range(counter):
            # igredient = dishes.readline().split(" | ")
            temp_list = []
            igredient_name, igredient_quantity, igredient_measure = dishes.readline().split(" | ")
            # print (igredient_name, igredient_quantity, igredient_measure)
            temp_list.append({'ingredient_name' : igredient_name, 'quantity' :  igredient_quantity, 'measure' : igredient_measure})
            print(temp_list)
        dishes.readline().strip()
