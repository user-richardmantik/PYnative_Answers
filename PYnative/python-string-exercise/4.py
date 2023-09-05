input_str = 'PyNaTive'

def get_lowercase_chars(input_str):
    output_list = list()
    for i in range(len(input_str)):
        if (input_str[i].islower()) :
            output_list.append(input_str[i])
        
    return output_list;

def get_uppercase_chars(input_str):
    output_list = list()
    for i in range(len(input_str)):
        if (input_str[i].isupper()) :
            output_list.append(input_str[i])
        
    return output_list;

output_list = get_lowercase_chars(input_str) + get_uppercase_chars(input_str)
print(''.join(output_list))