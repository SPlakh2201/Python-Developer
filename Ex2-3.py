List1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while List1[i] != 'градусов':
	temp_pos = ''
	if List1[i][0] == '+' or List1[i][0] == '-':
		temp_pos = List1[i][0]
		List1[i] = str(int(List1[i]))
	if List1[i].isdigit():
		if temp_pos == '+' or temp_pos == '-':
			if int(List1[i])//10 == 0:
				List1[i] = temp_pos + '0' + str(List1[i])
			else:
				List1[i] = temp_pos + str(List1[i])
		else:
			if int(List1[i])//10 == 0:
				List1[i] = '0' + List1[i]
		List1.insert(i, '"')
		List1.insert(i+2, '"')
		i += 2

	i += 1

print(' '.join(List1))