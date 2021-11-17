def log(func):
	def wrapper(*args):
		result = func(*args)
		print(result)
		print(*args)
		return(result)
	return wrapper

@log
def sum_two_numbers(a, b):
	return a+b

s = sum_two_numbers(7, 2)