matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

main = 1
collateral = 1
transponed_list = list() 
transponed = list()

for row in range(3):
	for column in range(3):
		if row == column:
			element = matrix[row][column]
			main *= element
		
		if row + column == 2:
			element = matrix[row][column]
			collateral *= element

det = main - collateral

for column in range(3):
	for row in range(3):
		element = matrix[row][column]
		transponed_list.append(element)
		if len(transponed_list) == 3:
			transponed.append(transponed_list)
			transponed_list =[]


print(transponed)

print(matrix)
print(det)
print(main)
print(collateral)