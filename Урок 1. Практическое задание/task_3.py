def company_profit1(dict1):
	answ = '' # O(1)
	list1_sorted = sorted(dict1, key = dict1.get, reverse = True) # O(N*log(N)) рискну предположить, что это так, ведь в нотации и в интернете ничего не нашёл о функции sorted()
	for i in range(0,3): # O(1)
		answ += f'{list1_sorted[i]} profit is {dict1[list1_sorted[i]]}\n' # O(1)
	return answ # O(1)

# Сложность алгоритма O(1) + O(N*log(N)) + O(1) + O(1) = O(1) + O(N*log(N))
# Итоговая сложность O(N*log(N))

def company_profit2(dict1):
	list1 = list(dict1.items()) # O(len(dict1.items()))
	repeat = 0 # O(1)
	while repeat != 3: # O(1)
		for i in range(len(list1)): # O(N)
			list1[i] = list(list1[i]) # O(1)
			count = 0 # O(1)
			for j in range(len(list1)): # O(N)
				if list1[i][1] > list1[j][1] or i == j: # O(1)
					count += 1 # O(1)
				else: # O(1)
					break # O(1)
			if count == 5: # O(1)
				repeat += 1 # O(1)
				print(list1[i][1]) # O(1)
				list1[i][1] = 0 # O(1)
				break # O(1)

# Итоговая сложность алгоритма: O(N^2)

company_dict = {'Company1' : 10, 'Company2' : 70, 'Company3' : 120, 'Company4' : 90, 'Company5' : 60}
company_profit2(company_dict)

# Вывод: Решение 1 является более эффективным, так как во 2-ом решении организовано 2 цикла for, в которых количество этераций одних и тех же действий будет 
# увеличиваться до тех пор, пока не будет найдено 3 максимальных элемента.
# А в решении 1 все эементы отсортированы(с помощью функции sorted) по убыванию и нам известно, сколько этераций должно повториться, чтобы завершить цикл for.
