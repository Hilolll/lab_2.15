#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание, Вариант № 15

# Написать программу, которая будет проходить по файлу с исходным кодом на Python и
# искать функции, не снабженные блоком комментариев. Можно принять за аксиому, что
# строка, начинающаяся со слова def, следом за которым идет пробел, будет считаться
# началом функции. И если функция документирована, предшествующая строчка должна
# начинаться со знака #. Перечислите названия всех функций, не снабженных
# комментариями, вместе с именем файла и номером строки, с которой начинается
# объявление функции. Одно или несколько имен файлов с кодом на языке Python
# пользователь должен передать в функцию в качестве аргументов командной строки. Для
# файлов, которые не существуют или не могут быть открыты, должны выдаваться
# соответствующие предупреждения, после чего должна быть продолжена обработка
# остальных файлов.

import argparse

parser = argparse.ArgumentParser(description='Find undocumented functions in Python code')
parser.add_argument('files', nargs='+', help='List of Python files to process')
args = parser.parse_args()


# Обработка каждого файла из списка
for file_name in args.files:
    try:
        with open(file_name, 'r') as file:
            # Чтение файла по строкам
            lines = file.readlines()

            # Цикл по строкам файла
            for i, line in enumerate(lines):
                if line.strip().startswith('def '):
                    if i > 0 and not lines[i - 1].strip().startswith('#'):
                        print(
                            f"Undocumented function '{line.split('(', 1)[0].split(' ')[1]}' in file '{file_name}' starting from line {i + 1}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except IOError:
        print(f"Could not open '{file_name}'.")