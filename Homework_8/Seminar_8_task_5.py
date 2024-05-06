"""
Напишите функцию, которая ищет json файлы в указанной директории 
и сохраняет их содержимое в виде одноимённых pickle файлов.

"""

import json
import pickle
import os

def json_to_pickle(directory='.'): # текущая директория
    for file in os.listdir(directory):
        file_name, file_exten = os.path.splitext(file)
        print(file_exten)
        if file_exten == '.json':
            with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
            with open(os.path.join(directory, file_name + '.pickle'), 'wb') as f:
                pickle.dump(data, f)

if __name__ == '__main__':
    json_to_pickle()
