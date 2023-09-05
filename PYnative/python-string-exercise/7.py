s1 = "Ynf"
s2 = "PYnative"

def is_balanced(input_str_1, input_str_2):
    is_balanced = True
    for c in input_str_1:
        if (input_str_2.find(c) == -1) :
            is_balanced = False
    
    return is_balanced

print(is_balanced(s1,s2))