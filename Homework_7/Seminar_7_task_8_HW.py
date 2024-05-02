"""
Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый номер.

принимать параметр количество цифр в порядковом номере.

принимать параметр расширение исходного файла. 
Переименование должно работать только для этих файлов внутри каталога.

принимать параметр расширение конечного файла.

принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 
из исходного имени файла. К ним прибавляется желаемое конечное имя, 
если оно передано. Далее счётчик файлов и расширение.

"""


import os
from pathlib import Path


def file_rename(directory, count_len: int, extension: str, new_extension: str, interval: list[int], new_name = ""):
    count = 0
    for file in os.listdir(directory):
        ext = file.rsplit('.')[-1]
        if ext == extension:
            count += 1
            os.rename(f"{directory}/{file}", 
                      f"{directory}/{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{count_len}}.{new_extension}")

if __name__ == '__main__':
    file_rename("files", 3, 'rnd', 'red', [0, 4], "new")