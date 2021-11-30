'''
Затестить def __str__(self):

к дажборду добавить метод, который будет выводить все таски + тест этого метода
это уже есть на гитхабе, можно скомуниздить

к дажборду добавить метод, который будет возвращаться все таски с одинаковым приоритетом
нужно сделать 2 таски в тесте с разными приоритетми (хотя бы 2) и удостовериться что он будет игнорить не нужную
'''
import googlemaps

class Maps:

    def __init__(self, key):
        self._client = googlemaps.Client(key=key)

    def __enter__(self):
        return self._client

    def __exit__(self, error_type, value, traceback):
        del self._client
        return True


class Task:

	def __init__(self, title):
		self.done = False
		self.title = title
		self._priority = 1 #может может иметь значения от 1 до 10 вспомнить такие ограничения / ответ уже ниже
		self.location = None

		#_ значит что атрибут скрытый, значит нужно образаться к геттер(property) и сеттер
		# такую же штуку с проверкой сделый для почты студента

	def __str__(self):
		return self.title

	@property
	def priority(self):
		return self._priority

	@priority.setter
	def priority(self, value):
		if value in range(1, 11):  #range не включает верхнюю границу, так что тут до 11
			self._priority = value  #ещё прикол в том что если поставить например 20, то тогда ветка выподняться не будет и останется 1, как значение по умол
		else:
			raise ValueError('Priority value is out of range (1-10)') #было return теперь тут выдает ошибку, это более корректно
	
	'''
	def add_location(self):
		place_lookup = input('Enter location name: \t')
		with Maps(key='AIzaSyC5lZ8gvA_9f6aovJMJD_bx0D7Y0dza3Dw') as gmaps:
			place = gmaps.find_place(
				place_lookup,
				'textquery',
				fields=['geometry/location', 'name', 'place_id']
				)
			if place['status'] == 'OK':
				self.location = {
				'coordinates': place['candidates'][0]['geometry']['location'],
				'name': place['candidates'][0]['name'],
				'google_id': place['candidates'][0]['place_id']
				}
	'''
	
	def add_location(self):
		place_lookup = input('Enter location name: \t')
		gmaps = googlemaps.Client(
			key = 'AIzaSyC5lZ8gvA_9f6aovJMJD_bx0D7Y0dza3Dw')
		try:
			place = gmaps.find_place(
				place_lookup,
				'textquery',
				fields = ['geometry/location', 'name', 'place_id']
			)
			if place['status'] == 'OK':
				self.location = {
					'coordinates': place['candidates'][0]['geometry']['location'],
					'name': place['candidates'][0]['name'],
					'google_id': place['candidates'][0]['place_id'],
				}
			else:
				raise RuntimeError('Cannot set location')
		except:
			return


class Dashboard:

	def __init__(self):
		self.task_list = []

	def add_task(self):
		title = input('Task name:    ')
		new_task = Task(title)
		self.task_list.append(new_task) 

	def print_all_tasks(self):
		for task in self.task_list:
			print(task)

	def print_tasks_with_same_priority(self):
		selected_priority = input('Please select a task priority (1-10):    ')
		for task in self.task_list:
			if selected_priority == task.priority:
				print(task)
			#придумать как сказать, что таких задач нет


	'''
	def search_by_title(self):
		search_title = input('Task name for search:    ')
		number_of_task = 0 
		search_task_title = ''
		for task in self.task_list:
			for letter_in_task in task.title:
				for letter in search_title:
					if letter_in_task == letter:
						search_task_title = search_task_title + letter_in_task
						if len(search_task_title)==len(search_title):
							search_task = task
							print(search_task)
							return task
					else:
						search_task_title=''
	'''
	def search_by_title(self):
		search_title = input('Task name for search:    ')
		for task in self.task_list:
			if search_title in task.title:
				print(task)
'''
task1 = Task('My first task')
task2 = Task('My second task')
task3 = Task('My third task')
dashboard = Dashboard()
dashboard.task_list.extend([task1, task2, task3])
dashboard.search_by_title()
'''












