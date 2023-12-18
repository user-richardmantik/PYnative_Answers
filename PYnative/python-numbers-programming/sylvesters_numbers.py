s_nums_dict = {}
s_nums_dict[0] = 2
def sylversters_number_seq(n, s_nums_dict):
    if (n in s_nums_dict.keys()):
        return s_nums_dict[n]
    else:
        curr_num = sylversters_number_seq(n-1, s_nums_dict) ** 2 - sylversters_number_seq(n-1, s_nums_dict) + 1

        s_nums_dict[n] = curr_num
        return curr_num


count_nums = int(input('Input : N = '))
print ('Output : ')
for n in range(0, count_nums):
    sylversters_number_seq(n, s_nums_dict)
print(' '.join([str(num) for num in s_nums_dict.values()]))