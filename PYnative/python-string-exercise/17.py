import re

input_str = 'Emma25 is Data scientist50 and AI Expert'
input_list = input_str.split()
output_list = []

for input_str in input_list:
    if (re.search(r'[a-zA-Z]+[0-9]+|[0-9]+[a-zA-Z]+', input_str) != None):
        output_list.append(input_str)

for output_str in output_list:
    print(output_str)