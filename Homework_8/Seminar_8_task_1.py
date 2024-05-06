"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл
с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла 
новый с данными в формате JSON. 
Имена пишите с большой буквы. 
Каждую пару сохраняйте с новой строки.

"""
import json

def text_to_json(file_name = 'res.txt'):
    with open(file_name, 'r', encoding='utf-8') as f, \
        open('res.json', 'w', encoding='utf=8') as f2:
        res_list = []
        for line in f:
            res_list.append(line.capitalize())
        json.dump(res_list, f2, indent=4) # indent=4 (4 пробела) для переноса строк в файле json

if __name__ == '__main__':
    text_to_json('res.txt')
