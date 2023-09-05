import math

s1 = 'Abc'
s2 = 'Xyz'

output_list = list()

s1_copy = s1
s2_copy = s2[::-1]

while(min(len(s1_copy), len(s2_copy)) > 0):
    output_list.append(s1_copy[0])
    output_list.append(s2_copy[0])
    s1_copy = s1_copy[1:]
    s2_copy = s2_copy[1:]

rest_chars = list()
if (len(s1) < len(s2)):
    rest_chars += s2_copy
elif (len(s1) > len(s2)):
    rest_chars += s1_copy

print(''.join(output_list + rest_chars))