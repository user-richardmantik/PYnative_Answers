def next_pascal_triangle_line(input_list):
    output_list = list()
    for i in range(0, len(input_list)):
        if (i > 0):
            output_list.append(input_list[i] + input_list[i-1])
        else:
            output_list.append(1)
    else:
        output_list.append(1)
        
    return output_list

def str_list(input_list):
    output_list = list()
    for num in input_list:
        output_list.append(str(num))
    return output_list

last_line_list = [1]
COUNT_ROWS = 7
for i in range(1, COUNT_ROWS + 1):
    print(' '.join(str_list(last_line_list)))
    last_line_list = next_pascal_triangle_line(last_line_list)