class Road:
	def __init__(self, length, width):
		self.__length = length
		self.__width = width
		self.__weight = 25
		self.__thickness = 5

	def show_result(self):
		return self.__length * self.__width * self.__weight * self.__thickness // 1000

A = Road(20, 5000)
print(f'{A.show_result()} т.')