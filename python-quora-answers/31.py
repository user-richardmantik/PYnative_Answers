start_num = 111
end_num = 999
answers = []

for num_i in range(start_num, end_num + 1):
    if (str(num_i).find('0') == -1):
        answers.append(num_i)

print('Answer =', len(answers))