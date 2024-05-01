"""
Задача 3.
Известно, что на доске 8×8 можно расставить 8 ферзей так, 
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, 
каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

"""

import random


def is_queen_beat(position: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return True  # ферзи не бьют друг друга
    else:
        return False  # ферзи бьют друг друга

def successful_position(count_successful):
    position = []
    n = 8
    count = 1
    count_iter = 0
    while count <= count_successful:
        count_iter += 1
        i = 0
        while i < n:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            if [x, y] not in position:
                position.append([x, y])
                i += 1

        if is_queen_beat(position):
            print(position, 'iter = ', count_iter)
            count += 1
        position.clear()

if __name__ == '__main__':
    print(is_queen_beat(input("Задайте координаты 8 ферзей:")))
    # Проверка:
    # print(is_queen_beat([[5, 2], [3, 5], [8, 3], [6, 4], [1, 1], [7, 6], [2, 7], [4, 8]]))
    # Возвращает True