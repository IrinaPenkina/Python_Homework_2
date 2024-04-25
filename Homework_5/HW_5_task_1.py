"""
Напишите функцию, которая принимает на вход строку — 
абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: 
путь, имя файла, расширение файла.

"""

import os
 
file_path = 'C:/Users/test.txt'
 
file_name = os.path.basename(file_path)
file = os.path.splitext(file_name) # tuple: [0] - name, [1] - extension
file_tuple = (file_path, file[0], file[1])
print(file_tuple)


