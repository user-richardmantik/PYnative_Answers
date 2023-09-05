def first_mid_last_chars(input_str):
    output_list = list()
    
    output_list.append(input_str[0])
    mid_index = int(len(input_str)/2);
    output_list.append(input_str[mid_index])
    output_list.append(input_str[-1])
    
    return output_list

def my_combine(input_list_1, input_list_2):
    output_list = list()
    for i in range(len(input_list_1)):
        output_list.append(input_list_1[i])
        output_list.append(input_list_2[i])
        
    return output_list

s1 = "America"
s2 = "Japan"
print(''.join(my_combine(first_mid_last_chars(s1), first_mid_last_chars(s2))))