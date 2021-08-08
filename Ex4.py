Staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for Person in Staff:
	Name = ''
	for i in range(len(Person)-1, 0, -1):
		if Person[i] != ' ':
			Name += Person[i]
		if Person[i] == ' ':
			Name = Name[::-1] + '!'
			break
	print('Привет,',Name)

