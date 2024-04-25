"""
Создайте функцию генератор чисел Фибоначчи

"""

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

generator_fibonacci = fibonacci()
for _ in range(int(input('Введите количество элементов последовательности: '))):
    print(next(generator_fibonacci), end=" ") 
