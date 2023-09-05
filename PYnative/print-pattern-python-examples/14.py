def str_list(input_list):
    output_list = list()
    for num in input_list:
        output_list.append(str(num))
    return output_list

COUNT_ROWS = 8

for i in range (0, COUNT_ROWS):
    line_list = []
    for j in range (0, i + 1):
        line_list.append((i+1) * (j+1))

    print(' '.join(str_list(line_list))) 