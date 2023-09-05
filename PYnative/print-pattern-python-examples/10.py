COUNT_ROWS = 4

numbers = range (1, 11)
z = 0
for i in range(0, COUNT_ROWS):
    line = ''
    for j in range (0, i+1):
        line = str(numbers[z]) + (' ' if (j > 0) else '') + line
        z += 1
    print (line)