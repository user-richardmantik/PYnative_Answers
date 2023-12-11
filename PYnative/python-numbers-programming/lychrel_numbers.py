MAX_ITERATIONS = 500

def is_palindrome_number(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if (num_str[i] == num_str[0-(i+1)]):
            continue
        else:
            return False
        
    return True

def reversed_number(num):
    if num < 0: return None;

    num_str = str(num)
    reversed_num_str = reversed(num_str)
    reversed_num = int(''.join(reversed_num_str))

    return reversed_num

def is_lychrel_number(num):
    for i in range(0, MAX_ITERATIONS):
        num = num + reversed_number(num)
        if (is_palindrome_number(num)): 
            return False
    
    return True

start_num = 0; end_num = 10000
for num in range(start_num, end_num + 1):
    if (is_lychrel_number(num)):
        print(num);

    num += 1