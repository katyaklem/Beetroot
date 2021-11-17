def linear_shift(array):
    print(array)
    zerro_element = array[0]
    if zerro_element > 0:
        zerro_element -= 1
    else:
        zerro_element == 0
    remove_element = array[len(array) - 1]
    array.remove(remove_element)
    array.insert(0, zerro_element)
    print(array)
    '''
    array = [1, 2, 3, 4] shift = 1 => [0, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [0, 0, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [0, 0, 0, 1]
    '''
    return array
 
array = [1, 2, 3, 4]
i = 0
while i < 4:    
    print(linear_shift(array))
    i+=1