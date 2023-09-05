import os

lines = []
i = 0
with open(os.getcwd() + "/test.txt", 'r') as fp:
    line = fp.readline().strip()
    while (line):
        if (i+1 != 5):
            lines.append(line)
        line = fp.readline().strip()
        i+=1

with open(os.getcwd() + '/new_file.txt', 'w') as fp:
    fp.writelines('\r\n'.join(lines))