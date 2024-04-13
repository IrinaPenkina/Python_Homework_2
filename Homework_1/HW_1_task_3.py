# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” 
# после каждой попытки. 

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT = 10
count = 1
num_guess = None

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
# print(num)

print('Угадай число между ', LOWER_LIMIT, 'и', UPPER_LIMIT, ' за 10 попыток.')

while count < COUNT + 1:
    print('Попытка', count)
    count += 1
    
    print('Введи число: ')
    num_guess = float(input())
    if num_guess < num:
        print('Искомое число больше.')
    elif num_guess > num:
        print('Искомое число меньше.')
    else:
        print('Поздравляю, ты угадал!')
        break

else:
    print('Исчерпаны все попытки. Сожалею.')
    print('Было введено число ', num, '.')
    quit()

