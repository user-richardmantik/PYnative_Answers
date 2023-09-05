COUNT_ROWS = 5

for i in range (COUNT_ROWS, 0, -1):
    line = ''
    for j in range (i, 0, -1):
        line += (' ' if (j < i) else '') + str(j)
    print (line)