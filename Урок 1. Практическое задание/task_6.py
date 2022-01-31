"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

class Tasks:
	def __init__(self):
		self.base = []
		self.remake = []


	def show_tasks(self):
		i = 0
		print("Base tasks:")
		for task in self.base:
			i += 1
			print(f'Task {i}: {task}')
		i = 0
		print('\n\nRemake tasks:')
		for task in self.remake:
			i += 1
			print(f'Task {i}: {task}')

	def add_task(self):
		choise = int(input('В какой список вы хотите добавить задачу?\nbase - 0, remake(Убедитесь что в списке Base присутсвуют задачи) - 1\nВаш выбор: '))
		if choise == 0:
			new_task = input('Введите новое задание: ')
			self.base.insert(0, new_task)
		elif choise == 1 and len(self.base) > 0:
			self.remake.insert(0, self.base.pop(0))


if __name__ == '__main__':
	tasks_list = Tasks()
	while True:
		choise = int(input('1. Добавить в список\n2. Показать списки\nВаш выбор: '))
		if choise == 1:
			tasks_list.add_task()
		elif choise == 2:
			tasks_list.show_tasks()
