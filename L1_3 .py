for procent_count in range(1, 101):
    if procent_count == 0:
    	print('У вас нет новых сообщений')
    elif procent_count == 1:
    	print(str(procent_count) + ' процент')
    elif procent_count < 5 :
    	print(str(procent_count) + ' процента')
    else:
        print(str(procent_count) + ' процентов')