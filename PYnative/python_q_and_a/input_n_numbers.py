count_num   = int(input('Input numbers: '))
numbers_str = str(input(''))

numbers     = [int(num) for num in numbers_str.split()]
numbers     = numbers[0:count_num]

print(numbers)