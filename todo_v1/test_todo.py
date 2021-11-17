import io
import unittest
from unittest.mock import patch, Mock

from Todo_LS17 import Task
from Todo_LS17 import Dashboard

LOCATION_DICT = {
    'candidates': [
        {'geometry': 
            {'location': {'lat': 50.5078373, 'lng': 30.4982641}
        },
        'name': 'ТРЦ DREAM / DREAM yellow', 
        'place_id': 'ChIJcZlrpBPS1EARl0pK1p4MO9Q'}
    ], 
    'status': 'OK'}

LOCATION_WITH_ERROR_DICT = {
    'candidates': [
        {'geometry': 
            {'location': {'lat': 50.5078373, 'lng': 30.4982641}
        },
        'name': 'ТРЦ DREAM / DREAM yellow', 
        'place_id': 'ChIJcZlrpBPS1EARl0pK1p4MO9Q'}
    ], 
    'status': 'ERROR'}



class TestTask(unittest.TestCase):

	def test_of_test(self):
		self.assertTrue(True)

	def test_task_object(self):
		task = Task('My test task')
		self.assertEqual(task.title, 'My test task') 
		self.assertFalse(task.done)

	def test_task_str(self):
		task = Task('My test task')
		self.assertEqual(str(task), 'My test task')

	def test_dashboard_object(self):
		dashboard = Dashboard()
		self.assertIsInstance(dashboard.task_list, list)
		self.assertEqual(len(dashboard.task_list), 0)

	@patch('builtins.input',return_value = 'My test task')
	def test_add_task(self,mock_input):
		dashboard = Dashboard()
		dashboard.add_task()
		self.assertEqual(len(dashboard.task_list), 1)
		self.assertEqual(dashboard.task_list[0].title,'My test task') 

	def test_get_task_priority(self):
		task = Task('My test task')
		self.assertEqual(task.priority, 1)

	def test_set_task_correct_priority(self):
		task = Task('My test task')
		task.priority = 5
		self.assertEqual(task.priority, 5)

	def test_set_task_incorrect_priority(self):
		task = Task('My test task')
		with self.assertRaises(ValueError):
			task.priority = 20
		self.assertEqual(task.priority, 1)

	@patch('sys.stdout', new_callable=io.StringIO)
	def test_print_all_tasks(self, mock_stdout):
		task1 = Task('My test task')
		task2 = Task('My second task')
		dashboard = Dashboard()
		dashboard.task_list.extend([task1, task2])
		dashboard.print_all_tasks()
		self.assertEqual(mock_stdout.getvalue(),'My test task\nMy second task\n')

	@patch('sys.stdout', new_callable=io.StringIO)
	@patch('builtins.input', return_value = 'second')
	def test_search_by_title(self, mock_input, mock_stdout):
		task1 = Task('My first task')
		task2 = Task('My second task')
		task3 = Task('My third task')
		dashboard = Dashboard()
		dashboard.task_list.extend([task1, task2, task3])
		dashboard.search_by_title()
		self.assertEqual(mock_stdout.getvalue(),'My second task\n')


	@patch('sys.stdout', new_callable=io.StringIO)
	@patch('builtins.input', side_effect = ['My first test task', 'My second test task', 'My third test task', 1])
	def test_print_tasks_with_same_priority(self, mock_input, mock_stdout):
		dashboard = Dashboard()
		i = 0
		while i < 3:
			dashboard.add_task()
			dashboard.task_list[i].priority = i+1
			i = i+1
		dashboard.task_list[2].priority = 1
		dashboard.print_tasks_with_same_priority()
		self.assertEqual(mock_stdout.getvalue(),'My first test task\nMy third test task\n')


	@patch('googlemaps.Client.find_place', return_value=LOCATION_DICT)
	@patch('builtins.input', return_value='Dream Town')
	def test_add_location(self, input_mock, maps_mock):
		task = Task('My test task')
		self.assertIsNone(task.location)
		task.add_location()
		self.assertIsNotNone(task.location)
		self.assertTrue('coordinates' in task.location)

	@patch('googlemaps.Client.find_place', return_value=LOCATION_WITH_ERROR_DICT)
	@patch('builtins.input', return_value='Dream Town')
	def test_add_location_with_error(self, input_mock, maps_mock):
		task = Task('My test task')
		self.assertIsNone(task.location)
		task.add_location()
		self.assertIsNone(task.location)




if __name__ == '__main__':
	unittest.main()