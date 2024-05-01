from Guess_number import guess_number
from Check_date import check_date

if __name__ == '__main__':
   num = int(input('Выберите номер: 1 для проверки даты или 2 для отгадывания числа: '))
   if num == 1:
      check_date(input("Задайте число в формате 'DD.MM.YYYY': "))
   elif num == 2:
      list = input("Задайте нижний лимит, верхний лимит, число попыток через пробел: ").split()
      lower_limit, upper_limit, count_trials = map(int, list)
      guess_number(lower_limit, upper_limit, count_trials)
   else:
      quit

