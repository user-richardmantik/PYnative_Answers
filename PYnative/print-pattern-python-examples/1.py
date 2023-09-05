COUNT_ROWS = 5

i = 1
while i <= COUNT_ROWS:
    line = ''
    j = 1
    while (j <= i):
        line = line + (' ' if (j > 1) else '') + str(i)
        j += 1
    i += 1
    print(line) 