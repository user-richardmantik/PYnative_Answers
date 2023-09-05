COUNT_ROW = 5

for i in range(COUNT_ROW):
    numbers = []
    for j in range (i+1):
        numbers.append(str(j+1))
    print(' '.join(numbers))