data = [8, 34, 5, 17, 46, 5, 78, 36, 8, 9, 54, 3, 0, 5, 71, 69, 11, 10, 37]

sort_data = []
simple_number =[]

serch_simple_number = 0
count_of_var = []

variability_firs_step = []

while data:
	first_number = data[0]
	for check_number in data:
		if check_number < first_number:
			first_number = check_number
	sort_data.append(first_number)
	data.remove(first_number)

print(sort_data)

for number in sort_data:
	for divider in range(1, len(sort_data)-1):
		if number % divider == 0:
			serch_simple_number += 1

	if serch_simple_number < 3:
		simple_number.append(number)

	serch_simple_number = 0

print(simple_number)

mean = sum(sort_data)/len(sort_data)
print(mean)

for number in sort_data:
	count_of_var.append(sort_data.count(number))
	max_count_index = count_of_var.index(max(count_of_var))

print(count_of_var)
print(max_count_index)

mode = sort_data[max_count_index]

print(mode)

for number in sort_data:
	variability_firs_step.append((number-mean)**2)

variability = sum(variability_firs_step) / len(sort_data)

print(variability)