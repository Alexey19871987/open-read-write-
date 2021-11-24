with open('рецепты.txt') as recipes:
    cook_book  = {}
    for dish in recipes:
        dish_name = dish.strip()
        quan_ingr = int(recipes.readline().strip())
        temp_data = []
        for ingr in range(quan_ingr):
            ingredient_name, quantity, measure = recipes.readline().split('|')
            structure = {'ingredient_name':ingredient_name,'quantity':quantity,'measure':measure}
            temp_data.append(structure)
            cook_book [dish_name] = temp_data
        recipes.readline()
    
list_dishs = ['Омлет']
persons = 2
def get_shop_list_by_dishes (list_dishs, persons):
    shop_list_by_dishes = {}
    for dish in list_dishs:
        
        for ingredient in cook_book[dish]:
            temp_dict = {}
            temp_dict['measure'] = ingredient['measure']
            temp_dict['quantity'] = int(ingredient['quantity'])* persons
            ingredients_name = ingredient['ingredient_name']
            if ingredients_name not in shop_list_by_dishes.keys():
                shop_list_by_dishes[ingredients_name] = temp_dict 
            else: 
                quantity_new = temp_dict['quantity']
                temp_dic_2 =shop_list_by_dishes[ingredients_name]
                quantity_old = temp_dic_2['quantity']
                temp_dict['quantity'] = quantity_old+quantity_new
                shop_list_by_dishes[ingredients_name] = temp_dict 
        return shop_list_by_dishes

import os
file_path = os.getcwd()
def files_txt(files_path):
    list_files = os.listdir(file_path)
    for file in list_files:
        if file.endswith('.txt') == False :
            list_files.remove(file)
    list_files.remove('result.txt')
    dict_files = {}
    for file in list_files:
        with open (f'{file_path}\{file}') as new_file :
            dict_files[len(new_file.readlines())] = file
    list_keys = sorted(dict_files.keys())
    dict_files_1 = {}
    for key in list_keys:
        dict_files_1[key] = dict_files[key]
    list_files = dict_files_1.items()
    for number, file in list_files:
        with open (f'{file_path}\{file}') as new_file :
            with open (f'{file_path}\\result.txt', 'a') as result_file:
                result_file.write(f"{file}\n")
                result_file.write(f"{number}\n")
                result_file.write(f"{new_file.read()}\n")



# {file} 
# {len(new_file.readlines())}
# {new_file.read()}

         
        
 
files_txt(file_path)
