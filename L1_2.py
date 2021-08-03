list_1 = []
sum_numbers1 = 0
sum_numbers2 = 0
for i in range (1, 1001, 2):
	number1 = i**3
	list_1.append(number1)
	digit1 = 0
	sum_digits1 = 0

	while number1 > 0:
		digit1 = number1 % 10
		sum_digits1 += digit1
		number1 //= 10

	number1 = i**3

	if sum_digits1 % 7 == 0 and sum_digits1 != 0:
		sum_numbers1 += number1


	number2 = i**3 + 17
	digit2 = 0
	sum_digits2 = 0

	while number2 > 0:
		digit2 = number2 % 10
		sum_digits2 += digit2
		number2 //= 10

	number2 = i**3 + 17

	if sum_digits2 % 7 == 0 and sum_digits2 != 0:
		sum_numbers2 += number2


print (sum_numbers1)
print (sum_numbers2)
