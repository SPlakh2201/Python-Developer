import os
import shutil


new_path = os.path.join('my_project', 'templates')
if not os.path.exists(new_path):
	os.mkdir(new_path)

for dirpath, dirnames, filenames in os.walk('my_project'):
	for file in filenames:
		if '.html' in file:
			src = os.path.join(dirpath, file)
			path_new = os.path.join(new_path, os.path.basename(dirpath))
			try:
				os.mkdir(path_new)
			except FileExistsError:
				pass
			try:
				shutil.copy(src, path_new)
			except:
				print('Папка templates уже существует.')
				exit(1)
			print(f'Файл {file} успешно скопирован.')