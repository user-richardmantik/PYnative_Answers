COUNT_ROWS = 5

for i in range (1, COUNT_ROWS+1):
    line_list = list()
    z = None
    for j in range (1, i+1):
        line_list.append(str(j))
        z = j
    for j in range(z, COUNT_ROWS):
        line_list.insert(0, ' ')
    line = ' '.join(line_list)
    print(line)