COUNT_ROWS = 5

i = COUNT_ROWS
while (i >= 1):
    line = ''
    j = 1
    while (j <= i):
       line = line + (' ' if (j > 1) else '') + str(j)
       j+=1
    print(line) 
    i-=1