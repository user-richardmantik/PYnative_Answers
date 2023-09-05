def print_divisible_by_5(input_list):
    print ('Given list is', input_list)
    print ('Divisible by 5')
    for num in input_list:
        if (num % 5 == 0):
            print(num)


num_list = [10, 20, 33, 46, 55]
print_divisible_by_5(num_list)