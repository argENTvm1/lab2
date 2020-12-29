"""
В этой подпрограмме обрабатываем файл: находим всевозможные жанры, категории,
платформы. Заносим все в множество(чтобы избежать повторений),а затем переводим
в строчный тип, чтобы использовать это в поиске по критериям, а также, чтобы
выводить это на экран для помощи пользователю.
"""

import csv

all_platforms_set = set()
all_categories_set = set()
all_genres_set = set()
category = ''
genre = ''


def find_all(set_name, iterated_obj):
    x = iterated_obj.split(';')
    for y in x:
        set_name.add(y)


with open('steam.csv', encoding='latin1') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'appid':
            continue
        find_all(all_platforms_set, row[6])
        find_all(all_categories_set, row[8])
        find_all(all_genres_set, row[9])
all_platforms_str = ''.join(i+'; ' for i in all_platforms_set)
all_categories_str = ''.join(i+'; ' for i in all_categories_set)
all_genres_str = ''.join(i+'; ' for i in all_genres_set)
