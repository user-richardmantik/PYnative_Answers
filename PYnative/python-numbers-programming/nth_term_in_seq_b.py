input_num = int(input('Input : n = '))
num = 0
pos = 0
while (True):
    num += 1
    pos += num
    if (pos >= input_num):
        break

print ('Output :', num)