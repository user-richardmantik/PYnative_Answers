import re
input_str = 'I am 25 years and 10 months old'

output_str = re.sub(r'[^\d]', '', input_str)
print(output_str)