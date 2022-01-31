"""
Задание 7.
Задание на закрепление навыков работы с деком
В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'
Но могут быть и такие палиндромы, как 'молоко делили ледоколом'
Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
Примечание:
Вам не нужно писать код с нуля. Вам нужно доработать пример с урока.
"""

class Palindrome:
	def __init__(self):
		self.elems = []

	def add_to_rear(self, elem):
		self.elems.insert(0, elem)

	def remove_from_front(self):
		return self.elems.pop()

	def remove_from_rear(self):
		return self.elems.pop(0)

	def size(self):
		return len(self.elems)


	def pal_checker(self, string):
		string = string.replace(" ", "")

		for el in string:
			self.add_to_rear(el)
		
		equal = True

		while self.size() > 1 and equal:
			first_symb = self.remove_from_front()
			last_symb = self.remove_from_rear()
			if first_symb != last_symb:
				equal = False

		return equal

if __name__ == '__main__':
	pal = Palindrome()
	check = input("Введите палиндром: ")
	print(pal.pal_checker(check))
