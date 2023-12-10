COUNT_NUMS  = 15
start_num   = 0

def is_narcissistic(num):
    if (num < 0): return False
    sum = 0

    num_str = str(num)
    len_num_str = len(num_str)
    for i in range(len_num_str):
        sum += int(num_str[i])**(len_num_str)
    
    return sum == num

n   = 0
num = start_num
while (n < COUNT_NUMS):
    if (is_narcissistic(num)):
        print(num)
        n += 1
    num += 1