"""
Напишите функцию, которая в бесконечном цикле запрашивает 
имя, личный идентификатор и уровень доступа (от 1 до 7). 

После каждого ввода добавляйте новую информацию в JSON файл. 

Пользователи группируются по уровню доступа.

Идентификатор пользователя выступает ключом для имени. 

Убедитесь, что все идентификаторы уникальны 
независимо от уровня доступа. 

При перезапуске функции уже записанные в файл данные 
должны сохраняться.
"""

import json
import os

def access_users(name='db.json'):
    db = {}
    if os.path.exists(name) and os.path.isfile(name):
        with open(name, 'r', encoding='utf-8') as f:
            db = json.load(f)
    with open(name, 'w', encoding='utf-8') as f:
        while True:
            while True:
                try: 
                    user_level = int(input('Введите число от 1 до 7 или любую букву для выхода: '))
                except:
                    json.dump(db, f) # записываем в json
                    exit() # выходим из программы
                else:
                    break # выходим из while true, делаем последующие проверки
            if not 1 <= user_level <= 7:
                continue
            if user_level not in db:
                db[user_level] = {}
            while True:
                try: 
                    user_id = int(input('Введите идентификатор: '))
                except:
                    print('Вы ввели не число!')
                else:
                    flag = False
                    for level in db:
                        for ident in db[level]:
                            print(ident)
                            if ident == user_id:
                                print('Идентификатор должен быть уникальным!')
                                flag = True
                                break # возвращаемся на while true
                    if flag:
                        continue
                    else:
                        break
            while True:
                user_name = input('Введите имя: ')
                if user_name: # проверка, что user_name не пустое
                    break
                else:
                    print('Имя не должно быть пустым.')
            db[user_level][user_id] = user_name

if __name__ == '__main__':
    access_users()
