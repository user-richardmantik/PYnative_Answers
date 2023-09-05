COUNT_ROWS = 5

for i in range(1, COUNT_ROWS + 1):
    line = ''
    for j in range(1, i+1):
        line = str(j) + (' ' if (j > 1) else '') + line
    print (line)