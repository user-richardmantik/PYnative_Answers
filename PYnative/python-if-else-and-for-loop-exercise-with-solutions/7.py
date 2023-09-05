COUNT_ROWS = 5

for i in range(0, COUNT_ROWS):
    numbers = []
    for j in range (0, i+1):
        numbers.insert(0, str(j+1))
    print(' '.join(numbers))