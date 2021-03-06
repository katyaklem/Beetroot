
import json
import csv

student_fields = ['first_name', 'last_name', 'gender', 'age', 'email', 'address']

EXAM=[]
STUDENTS = []
TEST_STUDENTS = [['Marry', 'Pop', 'F', '32', 'marry@pop', 'Od'],['Garry', 'Bob', 'M', '22', 'garry@bob', 'Bi']]

def add_student():
	student = {}
	for field in student_fields:
		student[field] = input('Enter {}'.format(field))
		if field == 'age':
			try:
				int(student['age'])
			except:
				student['age'] = input('Enter age as number\t')
	STUDENTS.append(student)

def load_students():
	for test_student in TEST_STUDENTS:
		student = dict(zip(student_fields, test_student))
		STUDENTS.append(student)

def dump_studens():
    with open('data/student_data.json', 'w') as file:
        json.dump(STUDENTS, file)

def dump_csv():
    with open('data/student_data.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=student_fields)
        writer.writeheader()
        for student in STUDENTS:
            writer.writerow(student)

def load_csv(file_path='data/student_data.csv'):
    with open(file_path, 'r') as read_file:
        STUDENTS.extend(csv.load(read_file))

def load_from_json(file_path='data/student_data.json'):
    with open(file_path, 'r') as read_file:
        STUDENTS.extend(json.load(read_file))

def print_student(student):
	max_len_fiels = max(len(field) for field in student_fields)
	for field in student:
		#while len(field) < max_len_fiels+1:
			#field += " "
		print(field.replace('_', ' ').capitalize(), student[field].capitalize())
		#field = field.replace('_', ' ').capitalize()
		#student[field] = student[field].capitalize()
		#print(field)
		#print(student[field])
		#print(max_len_fiels)
		
		#print("{: > max_len_fiels}, {: > max_len_fiels}".format(field, student[field]))

def print_students_list():
    for student in STUDENTS:
    	print('')
    	print('*************************')
    	print('')
    	print_student(student)

def calculator_avg_age():
	try:
		total_age = 0
		for student in STUDENTS:
			total_age += int(student['age'])
		avg_age = total_age // len(STUDENTS)
		print('Average age is {}'.format(avg_age))
	except ValueError:
		print('Cannot calculate average age')
	except Exception as e:
		print(str(e))

def firs_exam(file_exam = 'data/exam.json'):
	with open(file_exam, 'r') as read_file:
		EXAM.extend(json.load(read_file))
	print(EXAM)


ACTIONS ={
	'add': add_student,
	'load': load_students,
	'print': print_students_list,
	'age': calculator_avg_age,
	'dump': dump_studens,
    'dump_csv': dump_csv,
    'load_json': load_from_json,
    'load_csv': load_csv,
    'exam': firs_exam,
}

if __name__ == '__main__':
	while True:
		action = input('Your action:')
		if action in ACTIONS:
			ACTIONS.get(action)()
		else:
			break

#while True:
#	action = input('Your action:')
#	if action == 'add':
#		add_student()
#	elif action == 'load':
#		load_students()
#	elif action == 'print':
#		for student in STUDENTS:
#			print_student(student)
#	elif action == 'age':
#		calculator_avg_age()
#	elif action == 'all_student':
#		print_strudents_list()
#	else:
#		break


