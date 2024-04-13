# Напишите программу, которая принимает две строки вида 
# “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. 
# Для проверки своего кода используйте модуль fractions.


import fractions
import math

def cut_fraction(num: int, denom: int):
    gcd = math.gcd(num, denom)
    num_1 = int(num / gcd)
    denom_1 = int(denom / gcd)
    return str(num_1) + '/' + str(denom_1)

def sum_fractions(string_1, string_2):
    frac_1 = str_1.split('/')
    frac_2 = str_2.split('/')
    lcm_fraction = math.lcm(int(frac_1[1]), int(frac_2[1]))
    num_frac_1 = int(lcm_fraction / int(frac_1[1]) * int(frac_1[0]))
    num_frac_2 = int(lcm_fraction / int(frac_2[1]) * int(frac_2[0]))
    return cut_fraction(num_frac_1 + num_frac_2, lcm_fraction)

def mult_fractions(string_1, string_2):
    frac_1 = str_1.split('/')
    frac_2 = str_2.split('/')
    return cut_fraction(int(frac_1[0]) * int(frac_2[0]), int(frac_1[1]) * int(frac_2[1]))

str_1 = input('Задайте первую дробь в виде a/b: ')
str_2 = input('Задайте вторую дробь в виде a/b: ')
print('Сумма дробей: ', sum_fractions(str_1, str_2))
print('Произведение дробей: ', mult_fractions(str_1, str_2))
print ('Проверка с помощью модуля fractions:')
frac_1 = fractions.Fraction(str_1)
frac_2 = fractions.Fraction(str_2)
print('{} + {} = {}'.format(frac_1, frac_2, frac_1 + frac_2))
print('{} * {} = {}'.format(frac_1, frac_2, frac_1 * frac_2))
