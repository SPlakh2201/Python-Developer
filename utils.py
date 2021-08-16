import datetime
import requests

def get_content(xml):
	information = requests.get(xml)
	encode = requests.utils.get_encoding_from_headers(information.headers)
	content = information.content.decode(encoding=encode)
	return content


def currency_rates(chars, char):
	stop_char = chars.find(char)
	if stop_char != -1 and len(char) == 3:
		stop_value = chars.find('<Value>', stop_char)
		value = float(chars[stop_value + 7:chars.find('</Value>', stop_value)].replace(',', '.'))
	else:
		value = 'None'
	stop_date = chars.find('Date="')
	date = datetime.datetime.strptime(chars[stop_date + 6:chars.find('" name=')], '%d.%m.%Y')
	print(date.strftime('%b %d %Y'))
	return value