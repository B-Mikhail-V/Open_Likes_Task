# from pprint import pprint
# cook_book = {'Запеченный картофель': [{'ingredient_name': 'Картофель',
#                            'measure': 'кг',
#                            'quantity': '1'},
#                           {'ingredient_name': 'Чеснок',
#                            'measure': 'зубч',
#                            'quantity': '3'},
#                           {'ingredient_name': 'Сыр гауда',
#                            'measure': 'г',
#                            'quantity': '100'}],
#  'Омлет': [{'ingredient_name': 'Яйцо', 'measure': 'шт', 'quantity': '2'},
#            {'ingredient_name': 'Молоко', 'measure': 'мл', 'quantity': '100'},
#            {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': '2'}],
#  'Утка по-пекински': [{'ingredient_name': 'Утка',
#                        'measure': 'шт',
#                        'quantity': '1'},
#                       {'ingredient_name': 'Вода',
#                        'measure': 'л',
#                        'quantity': '2'},
#                       {'ingredient_name': 'Мед',
#                        'measure': 'ст.л',
#                        'quantity': '3'},
#                       {'ingredient_name': 'Соевый соус',
#                        'measure': 'мл',
#                        'quantity': '60'}],
#  'Фахитос': [{'ingredient_name': 'Говядина', 'measure': 'г', 'quantity': '500'},
#              {'ingredient_name': 'Перец сладкий',
#               'measure': 'шт',
#               'quantity': '1'},
#              {'ingredient_name': 'Лаваш', 'measure': 'шт', 'quantity': '2'},
#              {'ingredient_name': 'Винный уксус',
#               'measure': 'ст.л',
#               'quantity': '1'},
#              {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': '2'}],
#  'Фахитос_2': [{'ingredient_name': 'Говядина',
#                 'measure': 'г',
#                 'quantity': '300'},
#                {'ingredient_name': 'Перец сладкий',
#                 'measure': 'шт',
#                 'quantity': '2'},
#                {'ingredient_name': 'Винный уксус',
#                 'measure': 'ст.л',
#                 'quantity': '1'},
#                {'ingredient_name': 'Помидор',
#                 'measure': 'шт',
#                 'quantity': '3'}]}
#
# dish = ['Омлет', 'Омлет', 'Фахитос_2','Фахитос']
# dict_final = {} # Окончательный словарь продуктов
# dict_new = {} # Промежуточный словарь для наполнения в цикле
# for dish_order in dish:
#     for key, value in cook_book.items():
#         if key == dish_order:
#             print(key)
#             # dict_new = {}
#             for count in range(len(value)):
#                 # print(dict_new.keys())
#                 # print(value[count]['ingredient_name'])
#                 # print(value[count]['ingredient_name'] not in dict_new.keys())
#                 if value[count]['ingredient_name'] not in dict_new.keys():
#                     dict_new[value[count]['ingredient_name']] = {'quantity': value[count]['quantity'], 'measure': value[count]['measure']}
#                     dict_final.update(dict_new)
#                 else:
#                     # print(f"Сложить {value[count]['quantity'], dict_new[value[count]['ingredient_name']]['quantity'] }")
#                     new_quality = int(value[count]['quantity']) + int(dict_new[value[count]['ingredient_name']]['quantity'])
#                     dict_new[value[count]['ingredient_name']] = {'quantity': new_quality, 'measure': value[count]['measure']}
#                     dict_final.update(dict_new)
#
#
#             #     print(dict_final.update(dict_new))
#             # else:
#             #     print(dict_final)
#
# pprint(dict_final)

import os
from pprint import pprint
files_list = ['1.txt', '2.txt', '3.txt']
line_count_list = []
dict_texts = {}
for file in files_list:
    path = os.path.join(os.getcwd(), file)
    with open(path, encoding='utf-8') as text:
        text_text = text.readlines()
        line_count = len(text_text)
        line_count_list.append(line_count)
        dict_texts = {line_count: text_text}
        # pprint(line_count)
        # pprint(text_text)
pprint(dict_texts)
pprint(sorted(line_count_list))


