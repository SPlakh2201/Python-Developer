def odd_nums(n):
	for num in range(1, n + 1, 2):
		yield num

odd_to_n = odd_nums(int(input('Введите конечное значение: ')))

print(*odd_to_n, sep = '\n')