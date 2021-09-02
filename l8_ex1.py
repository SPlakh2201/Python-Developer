import re


def regular(expression):
	RE_EMAIL = re.compile('^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$')
	result = RE_EMAIL.match(expression)
	if result == None: 
		raise ValueError(f'wrong email: {expression}')
	else:
		return email_parse(expression)

def email_parse(email):
	separator = email.find('@')
	answ = {}
	answ['username'], answ['domain'] = email[:separator], email[separator + 1:]
	return answ


if __name__ == '__main__':

	email = str(input('Введите почту: '))
	print(regular(email))