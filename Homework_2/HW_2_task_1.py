# Напишите программу, которая получает целое число и возвращает 
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата. 

BASE = 16

number = int(input('Введите число: '))
print(hex(number))
digits = '0123456789abcdefghijklmnopqrstuvwxyz'
result = ''
while number > 0:
    result = digits[number % BASE] + result
    number //= BASE
print(result)