from utils import get_content, currency_rates


if __name__ == '__main__'
	string = str(input('Введите валюту: '))
	result = get_content('http://www.cbr.ru/scripts/XML_daily.asp')
	print(f'{string.upper()}: {currency_rates(result, string.upper())}\n')
	print(f'USD: {currency_rates(result, "USD")}\n')
	print(f'EUR: {currency_rates(result, "EUR")}\n')

# Использовать тип Decimal стоит, если необходимо производить
# расчёты, потому что такой тип данных более точен в вычислениях,
# но в данном случае он не нужен, так как для использования
# такого типа необходимо подключать модуль, что влияет на объём
# памяти, занимаемый кодом.