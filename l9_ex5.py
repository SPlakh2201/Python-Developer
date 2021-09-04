class Stationary:
	def __init__(self, title):
		self.title = title

	def draw(self):
		return 'Запуск отрисовки.'

class Pen(Stationary):
	def draw(self):
		return 'Уникальное сообщение класса Pen.'

class Pencile(Stationary):
	def draw(self):
		return 'Уникальное сообщение метода Pencile.'

class Handle(Stationary):
	def draw(self):
		return 'Уникальное сообщение метода Handle.'

print(Stationary().draw())
print(Pen().draw())
print(Pencile().draw())
print(Handle().draw())