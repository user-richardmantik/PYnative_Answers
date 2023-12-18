COUNT_NUMS = 17

recamans_numbers = [0]
last_r_num = 0
for n in range (1, COUNT_NUMS):
    r_num = last_r_num - n
    
    if (r_num not in recamans_numbers and r_num > 0 ):
        recamans_numbers.append(r_num)
    else:
        r_num   = last_r_num + n
        recamans_numbers.append(r_num)

    last_r_num = r_num

print (recamans_numbers)