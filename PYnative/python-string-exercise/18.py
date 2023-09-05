import re

input_str = '/*Jon is @developer & musician!!'
output_str = re.sub(r'[^\w\s]', '#', input_str)
print(output_str)