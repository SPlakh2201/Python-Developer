"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""

class StackOfPlates():
	def __init__(self):
		self.stacks = []


	def put_plates(self):
		limit = int(input("Enter limit of stack: "))
		count = int(input("Enter count of plates: "))
		remainder = count % limit
		count -= remainder
		for i in range(count//limit):
			self.stacks.append([" _ "] * limit)
		if remainder != 0:
			self.stacks.append([" _ "] * remainder)
		print(f'Put plates: {self.stacks}')


	def pop_plates(self):
		self.stacks[len(self.stacks)-1].pop()
		print(f'Pop last plate: {self.stacks}')

if __name__ == "__main__":
	stack = StackOfPlates()
	stack.put_plates()
	stack.pop_plates()
