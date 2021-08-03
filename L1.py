sec = int(input('Введите секунды: '))
days = 0
hours = 0
minutes = 0
seconds = 0
count_h = 1
count_m = 1
answer = ''

if sec // 60 >= 1:
	if sec // 3600 >= 1:
		if sec // 86400 >= 1:
			days = sec // 86400
			answer = str(days) + ' дн '
		hours = (sec - days * 86400) // 3600
		while hours > 59:
			hours -= 60
			count_h +=1
		answer += str(hours) + ' час '
	minutes = (sec - days * 86400 - hours * count_h * 3600) // 60
	while minutes > 59:
			minutes -= 60
			count_m +=1
	answer += str(minutes) + ' мин '
seconds = (sec - days * 86400 - hours * 3600 - minutes * count_m * 60)
answer += str(seconds) + ' сек'
print(answer)
