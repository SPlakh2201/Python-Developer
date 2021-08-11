from random import choice

def get_jokes(quan, rep):
	if quan > len(nouns) and rep == 0:
		print('У меня нет столько шуток. Доступно: ', len(nouns), '\nПоэтому выведу', len(nouns))
		quan = len(nouns)
	answ = []
	for i in range (0, quan):
		rand_nouns, rand_adverbs, rand_adjectives = choice(nouns), choice(adverbs), choice(adjectives)
		if rep == 0:
			nouns.remove(rand_nouns)
			adverbs.remove(rand_adverbs)
			adjectives.remove(rand_adjectives)
		answ.append(rand_nouns + ' ' + rand_adverbs + ' ' + rand_adjectives)
	return answ

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

quanity = int(input('Введте количество шуток: '))
repeat = int(input('Введите флаг "0", запрещающий повтор, или "1", разрешающий повторы: '))

print(get_jokes(quanity, repeat))
