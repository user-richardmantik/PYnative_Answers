COUNT_NUMS = 10

fibonacci_list = [0, 1]
for i in range (2, COUNT_NUMS):
    fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])


if (COUNT_NUMS > 1):
    fibonacci_list = [str(s) for s in fibonacci_list]
    print (' '.join(fibonacci_list))
elif (COUNT_NUMS == 1):
    print (0)
elif (COUNT_NUMS == 0):
    print ()