import csv
import file_processing # импорт обработанных данных

"""
1. Спрашиваем пользователя о его предпочтениях: платформа, жанр, категория,
формат распространения(платная, бесплатная), год выхода.
2. Проходясь по файлу циклом, ищем
"""

users_platform = 'Платформа'
users_genre = 'Жанр'
users_category = 'Категория'
result_games = 'Эти игры подходят вашим предпочтениям:'


def information_input(inputted_info, set_of_inputted_info, str_of_inputted_info):
    print(inputted_info + '?(Если не важно - оставить пустым). Не знаете какие? Напишите Help, чтобы узнать.')
    while True:
        inputted_info = input()
        if inputted_info == 'Help':
            print('Выберите из:', str_of_inputted_info)
        if inputted_info in set_of_inputted_info or inputted_info == '':
            break
        if inputted_info != 'Help':
            print('Неверный ввод! Введи одно из предложенных: '+str_of_inputted_info+'или оставь пустым.')
    return inputted_info


users_platform = information_input(users_platform, file_processing.all_platforms_set,
                                   file_processing.all_platforms_str)
users_genre = information_input(users_genre, file_processing.all_genres_set,
                                file_processing.all_genres_str)
users_category = information_input(users_category, file_processing.all_categories_set,
                            file_processing.all_categories_str)
print('Игра платная или бесплатная?(Если не важно - оставить пустым)')
while True:
    users_price = input()
    if users_price == 'Платная' or users_price == 'Бесплатная' or users_price == '':
        break
    print('Введи либо "Платная", либо "Бесплатная", либо оставь пустым.')
print('Укажи год, в котором игра вышла. Например, 2019 (Если не важно - введи 0)')
while True:
    try:
        users_year = int(input())
    except ValueError:
        print('Введи год! Только цифры, например, 2019 или 1999. Если не важно - введи 0')
    else:
        break

with open('steam.csv', encoding= 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        platform_from_file = row[6]
        genre_from_file = row[9]
        category_from_file = row[8]
        price_from_file = row[17]
        name_of_game = row[1]
        date_from_file = row[2]
        if (users_platform in platform_from_file and
           users_genre in genre_from_file and users_category in category_from_file):
            date = date_from_file.split('-')
            if ((users_price == 'Платная' and price_from_file != '0.0') or
               (users_price == 'Бесплатная' and price_from_file == '0.0') or
               users_price == ''):
                if users_year == 0:
                    result_games += '\n' + name_of_game
                elif date[0] == str(users_year):
                    result_games += '\n' + name_of_game
print(result_games)
with open('results.txt', 'w', encoding= 'utf-8') as file_results:
    file_results.write(result_games)
