# Напишите программу банкомат. 
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

from decimal import Decimal

MIN_SUM = 50
PROCENT_COMMISSION = 0.015
MIN_COMMISSION = 30
MAX_COMMISSION = 600
BONUS = 0.03
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = 0.1



def menu(balance: float, count: int, flag: bool):
    dict = {'1': 'пополнить счет',
           '2': 'снять со счета',
           '3': 'выйти из программы'
           }
    flag  = True
    for k, v in dict.items():
        if k.isdigit():
            print(f'{k} : {v}')
        else:
            print(v)
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_RATE)
        tax = Decimal(balance * TAX_RATE)
        print('Списан налог: ', tax.quantize(Decimal('1.00')))
    choice = input('Введите команду: ')
    if choice == '3':
        balance_2_digits = Decimal(balance)
        print('До свидания! Ваш баланс: ', balance_2_digits.quantize(Decimal('1.00')))
        flag  = False
        return balance, count, flag
    elif choice == '1':
        balance = give_money(balance)
        list_transactions.append(balance)
        count += 1
    elif choice == '2':
        balance = get_money(balance)
        list_transactions.append(balance)
        count += 1
    else:
        print('Неверная команда.')
    if count % 3 == 0:
        balance *= (1 + BONUS)
        print('Вам начислен бонус: ', round(balance*BONUS, 2))
    balance_2_digits = Decimal(balance)
    print('Ваш баланс: ', balance_2_digits.quantize(Decimal('1.00')))
    print('Изменения баланса: ', *list_transactions)
    return balance, count, flag

    pass

def get_money(balance: float):
    money_to_get = float(input('Введите сумму снятия, кратную 50: '))
    procent = money_to_get * PROCENT_COMMISSION

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMMISSION:
            procent = MIN_COMMISSION
        if procent > MAX_COMMISSION:
            procent = MAX_COMMISSION
        if money_to_get + procent <= balance:
            procent_2_digits = Decimal(procent)
            print('Комиссия за снятие: ', procent_2_digits.quantize(Decimal('1.00')))
            return balance - (money_to_get + procent)
        else:
            print ('Недостаточно средств для снятия.')
            return balance
     
    else: 
        print ('Ошибка снятия денег, сумма должна быть кратна 50. ')
        return balance
    pass

def give_money(balance: float):
    money_to_give = float(input('Введите сумму пополнения, кратную 50: '))
    if money_to_give % MIN_SUM == 0:
        return balance + money_to_give 
    else:
        print ('Сумма не кратна 50. Баланс не пополнен.')
        return balance
    pass


# if __name__ == 'main':
print('Добро пожаловать в банкомат!')
balance = 0
count = 0
flag = True
list_transactions = []
while flag:
    balance, count, flag = menu(balance, count, flag)
        
