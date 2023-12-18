COUNT_NUMS = 50

stern_brocot_numbers = [1, 1]

considered_index = 1

for n in range(2, COUNT_NUMS):
    if (n % 2 == 0):
        curr_num = stern_brocot_numbers[considered_index] + stern_brocot_numbers[considered_index-1]

        stern_brocot_numbers.append(curr_num) 
               
    else:
        curr_num = stern_brocot_numbers[considered_index]
        stern_brocot_numbers.append(curr_num)

        considered_index += 1

print(' '.join([str(num) for num in stern_brocot_numbers]))
