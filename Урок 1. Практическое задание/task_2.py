"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

# Алгоритм сложностью O(N):
def list_min1(numbers):
	min1 = numbers[0] # O(1)
	for number in numbers: # O(N)
		if number < min1: # O(1)
			min1 = number # O(1)
	return min1 # O(1)

# Алгоритм сложностью O(N^2):
def list_min2(num):
	min1 = num[0] # O(1)
	for i in range(len(num)): # O(N)
		for j in range(i+1, len(num)): #O(N)
			if num[i] > num[j] and num[j] < min1: #O(1)
				min1 = num[j] #O(1)
	return min1 #O(1)

print(list_min1([20, 10, 30, 100]))

print(list_min2([20, 10, 30, 100]))


