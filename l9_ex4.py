#basic class
class Car:
	#basic attributes
	def __init__(self):	
		self.speed = int(input('Введите скорость: '))
		self.color = input('Введите цвет: ')
		self.name = input('Введите название: ')
		self.is_police = True if input('Введите True, если машина полицейская: ') == 'True' else False
		
	#basic methods
	def go(self):
		print(f'{self.name} начала движение.')

	def stop(self):
		print(f'{self.name} остановилась.')

	def turn(self, direction):
		print(f'{self.name} повернула {direction}')

	def show_speed(self):
		print(f'Скорость: {self.speed}')

#child classes
class TownCar(Car):
	#redefined method
	def show_speed(self):
		if self.speed > 60:
			print('Вы превысили ограничение в 60км/ч.')

class SportCar(Car):
	pass

class WorkCar(Car):
	#redefined method
	def show_speed(self):
		if self.speed > 40:
			print('Вы превысили ограничение в 40км/ч.')

class PoliceCar(Car):
	pass

a = TownCar()
a.go()
a.turn('направо')
a.show_speed()

b = WorkCar()
b.go()
b.turn('налево')
b.show_speed()
b.stop()