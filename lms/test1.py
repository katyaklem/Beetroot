student_fields = ['first_name', 'last_name', 'gender', 'age', 'email', 'address']
STUDENTS = []
TEST_STUDENTS = [['Marry', 'Pop', 'F', '32', 'marry@pop', 'Od'],['Garry', 'Bob', 'M', '22', 'garry@bob', 'Bi']]
STUDENTS_WITHOUT_GROUP = []

class Student:

	def __init__(self, about_student):
		self.student_fields = ['first_name', 'last_name', 'gender', 'age', 'email', 'address']
		self.about_student = about_student
		self.student = dict(zip(student_fields, about_student))
		print(self.student)
		with open('data/student_data.json', 'w') as file:
        	json.dump(self.student, file)

	def info_about_student(self):
		student = self.student
		return(student)

	def comparison_age(self, second_student):
		print(self.student['first_name'],self.student['last_name'],self.student['age'])
		info_about_second = second_student.info_about_student()
		print(info_about_second['first_name'], info_about_second['last_name'],info_about_second['age'])
		if self.student['age'] > info_about_second['age']:
			print('{} older than {}'.format(self.student['first_name'], info_about_second['first_name']))
		elif self.student['age'] < info_about_second['age']:
			print('{} older than {}'.format(info_about_second['first_name'], self.student['first_name']))
		else:
			print('{} and {} are the same age'.format(self.student['first_name'], info_about_second['first_name']))

	def student_from_dict(cls, student_dict_data):
        new_student = cls()  
        for key in student_dict_data:
            setattr(new_student, key, dict_data[key])
        return new_student



class Group:

	def __init__(self, group_name, students_list):
		self.group_name = group_name
		self.students_list = students_list
		self.group = {group_name: students_list}
		print(self.group)

	def add_student_for_group(self, student):
		self.group[self.group_name].append(student)
		print(self.group)

class Lesson:
	
	def __init__(self, lesson_name, fio_student, date, attendance, assessment)
		self.lesson_name = lesson_name
		self.fio_student = fio_student
		self.date = date
		self.attendance = attendance
		self.assessment = assessment


def creat_a_new_student():
	student = []
	for field in student_fields:
		some_info = input('Enter {}'.format(field))
		if field == 'age':
			try:
				int(some_info)
			except:
				some_info = input('Enter age as number\t')
		elif field == 'first_name':
			if '@' in some_info == 0 or some_info[0] == '@' or some_info[len(some_info)-1] == '@':
				print('ERRRRRRROR')
				some_info = input('Enter correct email\t')
		student.append(some_info)
	return(student)


gr_name = 'IK 5.1.01'

first_student = ['Marry', 'Pop', 'F', '32', 'marry@pop', 'Od']
second_student = ['Garry', 'Bob', 'M', '22', 'garry@bob', 'Bi']

my_first_stud = Student(first_student)
my_second_stud = Student(second_student)
my_new_stud = Student(creat_a_new_student())

#my_gr = Group(gr_name, STUDENTS)

#test_student = my_first_stud.info_about_student()
#print(test_student)

#my_gr.add_student_for_group(test_student)

my_first_stud.comparison_age(my_second_stud)
