from pprint import pprint
cook_book = {'Запеченный картофель': [{'ingredient_name': 'Картофель',
                           'measure': 'кг',
                           'quantity': '1'},
                          {'ingredient_name': 'Чеснок',
                           'measure': 'зубч',
                           'quantity': '3'},
                          {'ingredient_name': 'Сыр гауда',
                           'measure': 'г',
                           'quantity': '100'}],
 'Омлет': [{'ingredient_name': 'Яйцо', 'measure': 'шт', 'quantity': '2'},
           {'ingredient_name': 'Молоко', 'measure': 'мл', 'quantity': '100'},
           {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': '2'}],
 'Утка по-пекински': [{'ingredient_name': 'Утка',
                       'measure': 'шт',
                       'quantity': '1'},
                      {'ingredient_name': 'Вода',
                       'measure': 'л',
                       'quantity': '2'},
                      {'ingredient_name': 'Мед',
                       'measure': 'ст.л',
                       'quantity': '3'},
                      {'ingredient_name': 'Соевый соус',
                       'measure': 'мл',
                       'quantity': '60'}],
 'Фахитос': [{'ingredient_name': 'Говядина', 'measure': 'г', 'quantity': '500'},
             {'ingredient_name': 'Перец сладкий',
              'measure': 'шт',
              'quantity': '1'},
             {'ingredient_name': 'Лаваш', 'measure': 'шт', 'quantity': '2'},
             {'ingredient_name': 'Винный уксус',
              'measure': 'ст.л',
              'quantity': '1'},
             {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': '2'}],
 'Фахитос_2': [{'ingredient_name': 'Говядина',
                'measure': 'г',
                'quantity': '300'},
               {'ingredient_name': 'Перец сладкий',
                'measure': 'шт',
                'quantity': '2'},
               {'ingredient_name': 'Винный уксус',
                'measure': 'ст.л',
                'quantity': '1'},
               {'ingredient_name': 'Помидор',
                'measure': 'шт',
                'quantity': '3'}]}

dish = ['Омлет', 'Фахитос', 'Фахитос_2']
dict_final = {}
dict_new = {}
for key, value in cook_book.items():

    if key in dish:
        # dict_new = {}
        for count in range(len(value)):
            print(dict_new.keys())
            print(value[count]['ingredient_name'])
            print(value[count]['ingredient_name'] not in dict_new.keys())
            if value[count]['ingredient_name'] not in dict_new.keys():
                dict_new[value[count]['ingredient_name']] = {'quantity': value[count]['quantity'], 'measure': value[count]['measure']}
            # print(value[count]['ingredient_name'])
        # if dict_new[value[count]['ingredient_name']] not in dict_final.keys():
                dict_final.update(dict_new)
            else:
                print("Сложить")

        #     print(dict_final.update(dict_new))
        # else:
        #     print(dict_final)

                pprint(dict_final)




