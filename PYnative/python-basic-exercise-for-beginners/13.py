COUNT_ROWS = 10;

for num_1 in range (1, COUNT_ROWS+1):
    print("{0:<2d}".format(num_1), end=' ')
    for num_2 in range (2, COUNT_ROWS+1):
        print(num_1 * num_2, end=' ')
    print()