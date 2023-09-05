import os


lines = []
i = 0
with open(os.getcwd() + "/test.txt", 'r') as fp:
    line = fp.readline().strip()
    while (line):
        lines.append(line)
        line = fp.readline().strip()
        i+=1

print (lines[3])