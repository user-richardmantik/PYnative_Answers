def is_palindrome_number(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if (num_str[i] == num_str[0-(i+1)]):
            continue
        else:
            return False
        
    return True

def print_is_palindrome_number(num):
    print ('original number', num)
    if (is_palindrome_number(num)):
        print('Yes. given number is palindrome number')
    else:
        print('No. given number is not palindrome number')
        
print_is_palindrome_number(121)
print()
print_is_palindrome_number(125)