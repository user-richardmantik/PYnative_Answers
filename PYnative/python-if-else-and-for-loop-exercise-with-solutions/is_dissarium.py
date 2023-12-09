def is_dissarium(num):
    sum = 0

    num_str = str(num)
    for i in range(len(num_str)):
        sum += int(num_str[i])**(i+1)
    
    return sum == num

num_array = [175, 25];
for num_i in num_array:
    if (is_dissarium(num_i)):
        print(num_i, 'is a dissarium number')
    else:
        print(num_i, 'is NOT a dissarium number')

