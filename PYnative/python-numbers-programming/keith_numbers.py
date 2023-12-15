import math

start_num = 10
end_num = 1000000

def get_digits(num):
    num_str = str(num)
    return [int(n) for n in num_str]

def is_keith(num):
    digits = get_digits(num)

    nums    = digits
    sum     = 0
    while (sum < num):
        sum     = int(math.fsum(nums))
        if (sum == num):
            return True
        nums.append(int(sum))
        nums.pop(0)
    
    return False

keith_numbers = []
for num_i in range(start_num, end_num):
    if (is_keith(num_i)):
        keith_numbers.append(num_i)

print(keith_numbers)