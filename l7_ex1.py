import os


if not os.path.exists('my_project'):
	os.makedirs(os.path.join('my_project', 'settings'))
	os.mkdir(os.path.join('my_project', 'mainapp'))
	os.mkdir(os.path.join('my_project', 'adminapp'))
	os.mkdir(os.path.join('my_project', 'authapp'))
	print('Структура папок создана.')
else:
	print('Папка уже существует!')