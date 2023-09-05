input_str = 'Apple'
input_dict = {}

for c in input_str:
    if (c not in input_dict.keys()) :
        input_dict[c]   = 1
    else:
        input_dict[c]   += 1

print(input_dict)