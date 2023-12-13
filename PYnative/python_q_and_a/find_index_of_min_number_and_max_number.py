import numpy

numbers_list = [3, 5, 2, 7, 5]

index_of_min_number = numpy.argmin(numbers_list) 
index_of_max_number = numpy.argmax(numbers_list)

print('Index of the MIN number in the list is', index_of_min_number)
print('Index of the MIN number in the list is', index_of_max_number)