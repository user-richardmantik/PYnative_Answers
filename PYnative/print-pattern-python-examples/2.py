COUNT_ROWS = 5

i = 1
while (i <= COUNT_ROWS):
    line = '';
    j = 1;
    while (j <= i):
        line += (' ' if (j > 1) else '') + str(j)
        j += 1
    print(line)
    i += 1