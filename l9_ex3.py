import sqlite3

def create_table(conn, cursor):
	cursor.execute("""CREATE TABLE IF NOT EXISTS worker_table (
		name VARCHAR,
		surname VARCHAR,
		position VARCHAR,
		wage INTEGER,
		bonus INTEGER	
	)""")

	conn.commit()


def add_worker():
	name = input('Name: ')
	surname = input('Surname: ')
	position = input('Position: ')
	wage = input('Wage: ')
	bonus = input('Bonus: ')
	conn.execute(f"INSERT INTO worker_table VALUES('{name}', '{surname}', '{position}', {wage}, {bonus})")
	conn.commit()


class Worker:
	def __init__(self, worker):
		self.name = worker[0]
		self.surname = worker[1]
		self.position = worker[2]
		self._income = {"wage": worker[3], "bonus": worker[4]}


class Position(Worker):
	def get_full_name(self):
		self.full_name = f'{self.name} {self.surname}'
		return self.full_name


	def get_total_income(self):
		self.total_income = 0
		for value in self._income.values():	
			self.total_income += value
		return self.total_income


if __name__ == '__main__':

	conn = sqlite3.connect('worker_sql.sqlite3')
	cursor = conn.cursor()
	create_table(conn, cursor)
	ask = int(input('Введите 0, если хотите добавить работника, 1 для вывода информации о работниках:\n'))
	if ask == 0:
		add_worker()
	elif ask == 1:
		for value in cursor.execute("SELECT * FROM worker_table"):
			A = Position(value)
			print(f'\nSurname: {A.get_full_name()}\nIncome: {A.get_total_income()}')
		
			