input_str = 'PYnative29@#8496'

count_digits = 0
sum_digits = 0

for c in input_str:
    if (c.isdigit()):
        sum_digits += int(c)
        count_digits += 1

print('Sum is:', sum_digits,  'Average is', (sum_digits/count_digits))