odd_to_n = (num for num in range(1, int(input('Введите конечное значение: ')) + 1, 2))
print(*odd_to_n, sep = '\n')