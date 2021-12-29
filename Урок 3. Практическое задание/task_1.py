"""
Задание 1.
Реализуйте:
a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.
"""
from time import time


def timer(function):
    def check_function(*args, **kwargs):
        start = time()
        func = function(*args, **kwargs)
        end = time()
        check = end - start
        print(f'{function.__name__} - {check} сек.')
        return func

    return check_function


@timer
def append_list(lst, count):
    for i in range(count):
        lst.append(i) # O(1)


@timer
def fill_dict(dictionary, count):
    for i in range(count):
        dictionary[i] = i # O(1)


@timer
def insert_list(lst, count):
    for i in range(count):
        lst.insert(0, i) # O(N)


lst = []
dictionary = {}
append_list(lst, 10000)
fill_dict(dictionary, 10000)
insert_list(lst, 10000)

"""
append_list - 0.0009899139404296875 сек.
fill_dict - 0.001001119613647461 сек.
insert_list - 0.06601691246032715 сек.

---

append_list - 0.0010004043579101562 сек.
fill_dict - 0.0020012855529785156 сек.
insert_list - 0.06501460075378418 сек.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.
ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

@timer
def edit_list(lst, count):
    for i in range(count):
        lst[i] = i + 1 # O(1)


@timer
def edit_dictionary(dictionary, count):
    for i in range(count):
        dictionary[i] = i + 1 # O(1)


edit_list(lst, 10000)
edit_dictionary(dictionary, 10000)


"""
edit_list - 0.0010004043579101562 сек.
edit_dictionary - 0.000989675521850586 сек.
---
edit_list - 0.0008938312530517578 сек.
edit_dictionary - 0.0019998550415039062 сек.
"""

@timer
def del_list(lst, count):
    for i in range(count):
        lst.pop(i) # O(N)


@timer
def del_dictionary(dictionary, count):
    for i in range(count):
        dictionary.pop(i) # O(1)


del_list(lst, 10000)
del_dictionary(dictionary, 10000)

"""
del_list - 0.048011064529418945 сек.
del_dictionary - 0.0009903907775878906 сек.
---
del_list - 0.04902291297912598 сек.
del_dictionary - 0.0019989013671875 сек.

---

Вывод: Заполнение списка при помощи функции append() происходит быстрее, если сравнивать с операцией для заполнения словаря по ключу, но незначительно.
Однако заполнения списка в начало с помощью функции insert() происходит значительно дольше, чем обе вышеупомянутые ф-ии, что подтверждает Big O.
Изменение списка по номеру элемента примерно выполняется за одно и то же время, что и изменения словаря по ключу, что подтверждает Big O.
Удаление элемента из списка по номеру элемента происходит значительно дольше, чем удаление элемента из словаря по ключу, что подтверждает Big O. 

Почему заполнение словаря по ключу выполняется дольше, чем заполнение списка с помощью функции append():
1. Вычисление хешей ключей словаря
2. У словаря данные хранятся в формате "ключ - значение", а с помощью функции append() список заполняется одним элементом в конец списка

Почему заполнение списка с помощью функции insert() выполняется дольше, чем заполнение списка с помощью функции append():
    C помощью функции append() список заполняется одним элементом в конец списка, а при использовании insert() новый элемент встаёт на указанную позицию, 
    сдвигая все следующие элементы вправо.

Почему удаление элемнтов списка выполняется дольше, чем удаление элементов словаря по ключу:
    При удалении элемента из списка, все следующие элементы смещаются влево, а элемент на указанной позиции удаляется.
"""
