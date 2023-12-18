#num_seq = [1]

next_num = 2
count_nums_encountered = 1

n = int(input('Input : n = '))
rem_n = n

while (count_nums_encountered < n):
    rem_n = n - count_nums_encountered

    count_nums_encountered += next_num
    next_num += 1

print('The {0}th number in the sequence is {1}.'.format(n, rem_n))