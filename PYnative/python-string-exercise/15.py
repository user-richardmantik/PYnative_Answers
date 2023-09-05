import re

input_str = "/*Jon is @developer & musician"
print('Original string is ', input_str)

# replace special symbols with ''
output_str = re.sub(r'[^\w\s]', '', input_str)
print('New string is', output_str)