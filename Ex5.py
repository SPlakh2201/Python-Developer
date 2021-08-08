Price_list = [158.258, 57.8, 46.01, 97, 8.05, 0, 98.4, 51, 2.2, 14.75, 48.74]

def PrintPrice(List):
	for Price in List:
		a = int(Price)
		b = int(round(Price - a, 2) * 100)
		if 0 <= b <= 9:
			answ2 = f'0{b} коп.'
		else:
			answ2 = f'{b} коп.'
		if 0 <= a <= 9:
			answ1 = f'0{a} руб.'
		else:
			answ1 = f'{a} руб.'
		print(answ1, answ2, end = ', ')


#Вывод через запятую по форату:
PrintPrice(Price_list)
print('ID списка:', id(Price_list))

#Вывод по возрастанию:
Price_list.sort()
print('\n\nПо возрастанию:')
PrintPrice(Price_list)
print('ID списка:', id(Price_list))

#По убыванию:
Price_list2 = list(reversed(Price_list))
print('\n\nПо убыванию:')
PrintPrice(Price_list2)
print('ID списка:',id(Price_list2), '\n\n')

#5 самых дорогих товаров:
print('5 самых дорогих товаров:')
PrintPrice(Price_list2[4::-1])