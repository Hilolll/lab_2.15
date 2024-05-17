#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание, Вариант № 15

# Написать программу, которая считывает текст из файла и выводит на экран сначала
# вопросительные, а затем восклицательные предложения

# Функция для определения типа предложения (? - вопросительное, ! - восклицательное)
def get_type(sentence):
    if sentence.endswith('?'):
        return '?'
    elif sentence.endswith('!'):
        return '!'
    else:
        return None

# Чтение текста из файла
file_path = 'example.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Разделение текста на предложения
sentences = [sentence.strip() for sentence in text.split('.')]

# Разделение по типу предложения
question_sentences = []
exclamation_sentences = []

for sentence in sentences:
    sentence_type = get_type(sentence)
    if sentence_type == '?':
        question_sentences.append(sentence)
    elif sentence_type == '!':
        exclamation_sentences.append(sentence)

# Вывод вопросительных предложений
print("Вопросительные предложения:")
for sentence in question_sentences:
    print(sentence)

# Вывод восклицательных предложений
print("\nВосклицательные предложения:")
for sentence in exclamation_sentences:
    print(sentence)