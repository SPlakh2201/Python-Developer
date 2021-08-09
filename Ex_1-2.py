def num_translate(num_string, dictionary):
	check = num_string
	num_string = num_string.lower()
	for key, val in dictionary.items():
		if num_string == key:
			answ = val
	if num_string not in dictionary.keys():
		answ = 'None'
	if check == check.title():
		answ = answ.title()
	return answ

Int_dict = {
	'null': 'ноль',
	'one': 'один',
	'two': 'два',
	'three': 'три',
	'four': 'четыре',
	'five': 'пять',
	'six': 'шесть',
	'seven': 'семь',
	'eight': 'восемь',
	'nine': 'девять'
}
while True:
	print(num_translate(str(input('Введите числительное: ')), Int_dict),'\n')