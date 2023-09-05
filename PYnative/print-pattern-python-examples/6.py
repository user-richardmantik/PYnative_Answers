COUNT_ROWS = 5

for i in range (0, COUNT_ROWS):
    line = ''
    for j in range (0, i+1):
        line += (' ' if (j > 0) else '') + str(2*i+1)
    print(line)