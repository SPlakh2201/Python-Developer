from time import sleep


class TrafficLight:
	def __init__(self):
		self.__colors = {'red': 7, 'yellow': 2, 'green': 6}

	def running(self):
		for color, time in self.__colors.items():
			print(color)
			sleep(time)

A = TrafficLight()
A.running()