def first_task(first_list):
	list_status = True
	for first_items in first_list:
		for second_items in (first_items+1, first_list):
			if first_items == second_items:
				list_status = False
			else: 
				list_status = True
	print(list_status)


test_list1 = [1, 2, 1]
test_list2 = [1, 2, 3]

first_task(test_list1)
first_task(test_list2)