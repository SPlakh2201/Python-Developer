# Решение 1.

def authentication(dict1): # Оценка алгоритма: O(13)
	login = input("\nEnter your username: ") # O(1)
	if login in dict1.keys(): # По информации в интернете: O(1) + O(1) 
		password = input("Enter your password: ") # O(1)
		if password == dict1[login]: # O(1)
			return 'Succes' # O(1)
		else: # подозреваю, что O(1)
			return 'Wrong password' # O(1)
	else: # O(1)
		registration(login, dict1) # O(3)
		return 'Welcome' # O(1)


def registration(key, dict1): 
	password = input("You are not registered. Enter your password for registration: ") # O(1)
	dict1.setdefault(key, password) # O(1) 
	print(f'{users[key]} your password') # O(1)


# Решение 2.

def authentication2(dict1): # Оценка сложности: O(N)
	login = input("\nEnter your username: ") # O(1)
	if login in dict1.keys(): # O(1) + O(1)
		for key, value in dict1.items(): # O(N)
			if key == login: # O(1)
				password = input("Enter your password: ") # O(1)
				if value == password: # O(1)
					return 'Succes' # O(1)
				else: # O(1)
					return 'Wrong password' #O(1)
	else: # O(1)
		registration(login, dict1) #O(3)
		return 'Welcome' # O(1)


users = {'qwe': '123'}
while True:
	print(authentication2(users))


# Вывод: Решение 1 является более эффективным, так как, в отличие от решения 2, оно не использует циклов.
# Бесконечный цикл while для тестирования программы и в алгоритм он не входит.
