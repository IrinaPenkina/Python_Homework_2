'''
Задача 2
Напишите функцию принимающую на вход только ключевые параметры 
и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''


def reverse_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(reverse_dict(year=2024,
                     months=['January', 'February', 'March'],
                     weeks=[3, 6, 7, 9],
                     days=['Mon', 'Wed', 'Fri', 'Sun']))

