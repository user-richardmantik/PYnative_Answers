def str_list(input_list):
    output_list = list()
    for num in input_list:
        output_list.append(str(num))
    return output_list

SIDE = 5;
last_line_list = list()
for i in range (0, SIDE):
    last_line_list.append(i+1)

for i in range(0, SIDE):
    for j in range(0, i+1):
        last_line_list[j] = i+1
    print (' '.join(str_list(last_line_list)))