student_fields = ['first_name', 'last_name', 'gender', 'age', 'email', 'address']

STUDENTS = []
TEST_STUDENTS = [['Marry', 'Pop', 'F', '32', 'marry@pop', 'Od'],['Garry', 'Bob', 'M', '22', 'garry@bob', 'Bi']]

def add_student():
	student = {}
	for field in student_fields:
		student[field] = input('Enter {}'.format(field))
	STUDENTS.append(student)

def print_student(student):
	max_len_fiels = max(len(field) for field in student_fields)
	for field in student:
		#while True:
		#	if len(field) < max_len_fiels:
		#		field += ' '
		#	else:
		#		break
		print(field.replace('_', ' ').capitalize(), student[field].capitalize())

def load_students():
	for test_student in TEST_STUDENTS:
		student = dict(zip(student_fields, test_student))
		STUDENTS.append(student)

def calculator_avg_age():
	total_age = 0
	for student in STUDENTS:
		total_age += int(student['age'])
	avg_age = total_age // len(STUDENTS)
	print(avg_age)


while True:
	action = input('Your action:')
	if action == 'add':
		add_student()
	elif action == 'load':
		load_students()
	elif action == 'print':
		for student in STUDENTS:
			print_student(student)
	elif action == 'age':
		calculator_avg_age()
	else:
		break


