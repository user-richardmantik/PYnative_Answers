input_str = "James"
output_list = list();
output_list.append(input_str[0]);

mid_index = int(len(input_str)/2);
output_list.append(input_str[mid_index])
output_list.append(input_str[-1])
print(''.join(output_list))