my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numbers_at_odd_index_list = []
for i in range(len(my_list)):
    if (i % 2 != 0):
        numbers_at_odd_index_list.append(my_list[i])

print (' '.join([str(n) for n in numbers_at_odd_index_list]))