"""
Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.

"""
from collections import Counter

lst = [1, 5, 3, 4, 2, 1, 5, 'hi', 'home', 'hi']

dict = (Counter(lst))
new_lst = []
for k, v in dict.items():
    if v > 1:
        new_lst.append(k)
# print(dict)
print(new_lst)
