"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import Timer, timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(count, nums):
    new_arr = [0]
    for i in range(count):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


if __name__ == '__main__':
    count = int(input('Введите кол-во элементов: '))
    lst = [i+1 for i in range(count)]
    t1 = Timer(f"func_1({lst})", setup="from __main__ import func_1")
    print(f"func_1 - {t1.timeit(number=100000)} seconds")

    t2 = Timer(f"func_2({count}, {lst})", setup="from __main__ import func_2")
    print(f"func_2 - {t2.timeit(number=1000)} seconds")

"""
Введите кол-во элементов: 654
func_1 - 13.5237042 seconds
func_2 - 0.13356929999999778 seconds

Изменения:
Избавление от функции len() путём введения новой переменной count, которую пользователь вводит с клавиатуры, что позволяет значительно сократить время выполнения алгоритма.
"""
