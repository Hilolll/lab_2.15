#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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