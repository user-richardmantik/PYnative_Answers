def first_last_same(input_list):
    print ('Given list', input_list)
    if (input_list[0] == input_list[len(input_list) - 1]):
        return True
    else:
        return False
    
numbers_1 = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_1))

numbers_2 = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_2))