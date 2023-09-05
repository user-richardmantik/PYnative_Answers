COUNT_ROWS = 5

for i in range(COUNT_ROWS, 0, -1):
    line = ''
    for j in range(0, i+1, 1):
        line += (' ' if (j >= 1) else '') + str(j)
    print (line)