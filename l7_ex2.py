import os
import yaml


if not os.path.exists('config.yaml'): 
	config = {'my_project': 
	[{'settings': 
		['__init__.py', 'dev.py', 'prod.py']}, 
	{'mainapp': 
		['__init__.py', 'models.py', 'views.py', 
		{'templates': 
			[{'mainapp': ['base.html', 'index.html']}]}]},
	{'authapp': 
		['__init__.py', 'models.py', 'views.py', 
		{'templates': 
			[{'authapp': 
				['base.html', 'index.html']}]}]}]}
	with open('config.yaml', 'w') as f:
		f.write(yaml.dump(config))
	print('Файл config.yaml успешно создан.')
else:
	print('Файл config.yaml уже существует!')


if not os.path.exists('my_project'):
	with open('config.yaml', 'r') as f:
		config = yaml.load(f, Loader = yaml.FullLoader)
		for direction1, content1 in config.items():
			folder1 = direction1
			os.mkdir(folder1)
			for relist1 in content1:
				for direction2, content2 in relist1.items():
					folder2 = os.path.join(folder1, direction2)
					os.mkdir(folder2)
					for relist2 in content2:
						if '.py' in relist2:
							with open (os.path.join(folder2, relist2), 'w') as f:
								pass
						if not '.py' in relist2:
							for direction3, content3 in relist2.items():
								folder3 = os.path.join(folder2, direction3)
								os.mkdir(folder3)
								for relist3 in content3:
									if not '.html' in relist3:
										for direction4, content4 in relist3.items():
											folder4 = os.path.join(folder3, direction4)
											os.mkdir(folder4)
											for relist4 in content4:
												if '.html' in relist4:
													with open (os.path.join(folder4, relist4), 'w') as f:
														pass
	print('Папка my_project успешно создана.')
else:
	print('Папка my_project уже существует.')