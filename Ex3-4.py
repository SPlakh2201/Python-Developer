def thesaurus_adv(FIO):
	print(FIO)
	Dict_FIO = {}
	for name in FIO:
		List_FIO_i = name.split(' ')
		if List_FIO_i[1][0] in Dict_FIO.keys():
			Dict_FIO[List_FIO_i[1][0]].append(name)
		else:
			Dict_FIO[List_FIO_i[1][0]] = []
			Dict_FIO[List_FIO_i[1][0]].append(name)
	return Dict_FIO


Str_FIO = str(input('Введите данные через запятую:\n'))
FIO = Str_FIO.split(', ')
print(thesaurus_adv(FIO))