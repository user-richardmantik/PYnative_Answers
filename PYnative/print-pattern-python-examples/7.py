COUNT_ROWS = 5

for i in range(COUNT_ROWS, 0, -1):
    line = ''
    for j in range(0, i):
        line += (' ' if (j > 0) else '') + str(i)
    print (line)