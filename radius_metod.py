print('Привет, я калькулятор на минималках, поэтому я умею считать только степени целых чисел.')
list_of_numbers_string = input('Введи какой-то список целых чисел через пробел:')
degree = int(input('Теперь введи степень:'))

def exponentiation(some_numbers, some_degree):
	some_numbers_ints = ([int(number) for number in some_numbers.split(' ')])
	some_numbers_exponentiation = ([number**some_degree for number in some_numbers_ints])
	print(some_numbers_exponentiation)
	print(some_numbers_ints)

exponentiation(list_of_numbers_string, degree)
