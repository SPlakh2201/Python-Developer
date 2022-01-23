"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""

from collections import defaultdict as dedict


def translate16(integer, numb):
    answ = 0
    for i in range(len(integer)):
        try:
            numb1 = int(integer[i])
        except ValueError:
            numb1 = numb[integer[i]]
        finally:
            answ += numb1 * 16 ** (len(integer) - 1 - i)

    return answ


def translate10(integer, numb):
    answ = ""
    while integer != 0:
        remainder = integer % 16
        if remainder in numb.values() and remainder < 16:
            for k, v in numb.items():
                if remainder == v:
                    answ += k
        else:
            answ += str(remainder)
        integer //= 16
    return answ[::-1]


numb = dedict()
numb['A'] = 10
numb['B'] = 11
numb['C'] = 12
numb['D'] = 13
numb['E'] = 14
numb['F'] = 15

int1 = input("Введите 1-ое число: ")
int2 = input("Введите 2-ое число: ")

answ1 = translate16(int1, numb)
answ2 = translate16(int2, numb)

summ = answ1 + answ2
multi = answ1 * answ2

print(f"Сумма чисел {int1}({answ1}) и {int2}({answ2}): {translate10(summ, numb)}")
print(f"Произведение чисел {int1}({answ1}) и {int2}({answ2}): {translate10(multi, numb)}")
