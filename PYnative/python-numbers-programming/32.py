total = 0
for num_i in range(1,2023+1,2):
    total += (num_i ** num_i)

print('Remainder =', total % 2025)