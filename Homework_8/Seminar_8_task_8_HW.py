"""
Напишите функцию, которая получает на вход директорию и 
рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle. 

Для дочерних объектов указывайте родительскую директорию. 

Для каждого объекта укажите файл это или директория.

Для файлов сохраните его размер в байтах, 
а для директорий размер файлов в ней с учётом всех 
вложенных файлов и директорий.

"""
import os
from pathlib import Path
import json
import csv
import pickle


def dir_size(path) -> int:
    """Вычисление размера папки в байтах с учетом вложенных папок и файлов"""
    folder_size = 0
    num_files = 0
    iteration = 0
    for file in Path(path).rglob('*'):
        if (os.path.isfile(file)):
            folder_size += os.path.getsize(file)
            num_files += 1
        iteration += 1
    return folder_size


def dir_count_obj(path) -> int:
    """Вычисление количества папок и файлов в заданной директории с учетом вложенности"""
    list_obj_names = []
    dir_list = Path('directory').rglob('*')
    for obj in dir_list:
        obj_name = Path(obj).name 
        if os.path.isdir(obj) or os.path.isfile(obj):
            list_obj_names.append(obj_name)
    return len(list_obj_names)


def dir_tree_to_csv_file(directory='directory', file='dir_tree_csv.csv') -> None:
    """Вывод папок и файлов директории, их размера и родительской директории в файл формата csv"""
    with open(file, 'w', encoding='utf-8') as f:
        dir_list = Path('directory').rglob('*')
        count = 0
        f.write('obj_name,' 'obj_type,' 'obj_size,' 'upper_folder')
        f.write('\n')
        for obj in dir_list: 
            obj_name = Path(obj).name
            if os.path.isdir(obj):
                obj_type = 'dir'
                obj_size = dir_size(obj)
            elif os.path.isfile(obj):
                obj_type = 'file'
                obj_size = os.path.getsize(obj)
            else:
                continue
            upper_folder = Path(obj).parent
            count += 1
            f.write(f'{obj_name},{obj_type},{obj_size},{upper_folder}')
            f.write('\n' if count < dir_count_obj(directory) else "")


def csv_to_json(from_file='dir_tree_csv.csv', to_file='dir_tree_json.json') -> None:
    """Конвертация файла формата csv в файл формата json"""
    json_list = []
    with open(from_file, 'r', newline='', encoding='utf-8') as f:
        csv_write = csv.reader(f, dialect='excel')
        for i, line in enumerate(csv_write):
            json_dict = {}
            if i == 0:
                continue
            else:
                obj_name, obj_type, obj_size, upper_folder = line
                json_dict['obj_name'] = line[0]
                json_dict['obj_type'] = line[1]
                json_dict['obj_size'] = int(line[2])
                json_dict['upper_folder'] = line[3]
                json_list.append(json_dict)
    with open(to_file, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)


def json_to_pickle(from_file='dir_tree_json.json', to_file='dir_tree_pickle.pickle') -> None:
    """Конвертация файла формата json в файл формата pickle"""
    with open(from_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(to_file, 'wb') as f:
        pickle.dump(data, f)

if __name__ == '__main__':
    dir_tree_to_csv_file()
    csv_to_json()
    json_to_pickle()
    
