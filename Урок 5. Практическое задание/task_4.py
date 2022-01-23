"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

simple_dict = dict()
ordered_dict = OrderedDict()

def fill_dict(dicti):
    for i in range(0, 50):
        dicti.setdefault(i, i**2)
    return dicti


def change_dict(dicti):
    for i in range(0, 50):
        dicti[i] = i**2 + 1
    return dicti


def pop_dict(dicti):
    for i in range(0, 50):
        dicti.pop(i, i**2)
    return dicti

print(timeit("fill_dict(simple_dict)", globals=globals())) # 18.3842076
print(timeit("fill_dict(ordered_dict)", globals=globals())) # 18.156303
new_simple_dict = fill_dict(simple_dict)
new_ordered_dict = fill_dict(ordered_dict)
print(timeit("change_dict(new_simple_dict)", globals=globals())) # 17.8900274
print(timeit("change_dict(new_ordered_dict)", globals=globals())) # 18.4654769

print(timeit("pop_dict(new_simple_dict)", globals=globals())) # 17.273736800000002
print(timeit("pop_dict(new_ordered_dict)", globals=globals())) # 22.631619399999998

"""
Вывод: Использование упорядоченного словаря при работе с большим кол-вом данных не имеет смысла, так как использование обычного словаря быстрее практически всегда,
однако при работе с небольшим количеством данных, а также при необходимости подчеркнуть в коде обязательность порядка в словаре, стоит использовать упорядоченный словарь.
"""
