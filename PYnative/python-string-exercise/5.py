input_str = "P@#yn26at^&i5ve"

def count_alphas(input_str):
    output_list = list()
    for c in input_str:
        if (c.isalpha()):
            output_list.append(c)

    return len(output_list)

def count_digits(input_str):
    output_list = list()
    for c in input_str:
        if (c.isdigit()):
            output_list.append(c)

    return len(output_list)

def count_symbols(input_str):
    output_list = list()
    for c in input_str:
        if (not c.isalpha() and not c.isdigit()):
            output_list.append(c)

    return len(output_list)

print('total counts of Chars, Digits, and Symbols')
print()
print('Chars =', count_alphas(input_str))
print('Digits =', count_digits(input_str)) 
print('Symbol =', count_symbols(input_str))