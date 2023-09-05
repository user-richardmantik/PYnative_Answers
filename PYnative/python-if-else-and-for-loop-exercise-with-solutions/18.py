import math

COUNT_ROWS = 9
COUNT_COLS = math.ceil(COUNT_ROWS / 2)
i = 0
while (i < COUNT_COLS):
    print ('* ' * (i+1))
    i += 1
while (i >= 0):
    print ('* ' * (i+1))
    i -= 1