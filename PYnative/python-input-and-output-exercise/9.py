import os

file_size = os.stat('test.txt').st_size
if file_size == 0:
    print ('file is empty')