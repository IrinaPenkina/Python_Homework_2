"""
Напишите функцию, которая заполняет файл 
(добавляет в конец) случайными парами чисел. 
Первое число int, второе - float разделены вертикальной чертой. 
Минимальное число - -1000, максимальное - +1000. 
Количество строк и имя файла передаются как аргументы функции. 

"""

import os
import random as rd


MIN_NUMBER = -1000
MAX_NUMBER = 1000


def generate_numbers(line_count:int, file_name: str ):
    """Заполняет файл числами."""
    with open(file_name, 'w', encoding='utf-8') as f:
        for count in range(line_count):
            f.write(f'{rd.randint(MIN_NUMBER, MAX_NUMBER)}|{rd.random() * 2000 - 1000}')
            f.write('\n' if count < line_count - 1 else '') # чтобы не создавал пустую строку в конце

if __name__ == '__main__':
    generate_numbers(10, 'data_1.txt')