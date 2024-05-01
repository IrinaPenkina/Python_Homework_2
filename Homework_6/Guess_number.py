"""
Улучшаем задачу 2. 
Добавьте возможность запуска функции “угадайки” из модуля 
в командной строке терминала. 
Строка должна принимать от 1 до 3 аргументов: 
параметры вызова функции. 
Для преобразования строковых аргументов командной строки 
в числовые параметры используйте генераторное выражение.

"""

from random import randint
from sys import argv

def guess_number(lower_limit=0, upper_limit=100, count_trials=5): 
    num = randint(lower_limit, upper_limit)
    print(f'Угадай число между {lower_limit} и {upper_limit} за {count_trials} попыток.')
    count = 1
    num_guess = None
    while count < count_trials + 1:
        print('Попытка', count)
        print('Введи число: ')
        num_guess = float(input())
        if num_guess < num:
            print('Искомое число больше.')
        elif num_guess > num:
            print('Искомое число меньше.')
        else:
            print('Поздравляю, ты угадал!')
            break
        count += 1
    else:
        print(f'Вы исчерпали {count_trials} попыток. Сожалею.')
        print(f'Было задумано число {num}.')
    quit()


if __name__ == '__main__':
    print(argv)
    guess_number(*map(int, argv[1:]))


