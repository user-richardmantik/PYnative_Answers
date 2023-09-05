import math

input_str = "JhonDipPeta"
l_index = math.floor((len(input_str) - 3) / 2)
r_index = len(input_str) - math.ceil((len(input_str) - 3) / 2)
print (input_str[l_index: r_index])