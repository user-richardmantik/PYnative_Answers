import math

COUNT_NUMS = 10
moser_de_bruijn_numbers = [0, 1]
for n in range(2, COUNT_NUMS):
    if (n % 2 == 0):
        nth_mdb_num = moser_de_bruijn_numbers[math.floor(n/2)] * 4
    else:
        nth_mdb_num = moser_de_bruijn_numbers[math.floor(n/2)] * 4 + 1
    moser_de_bruijn_numbers.append(nth_mdb_num)

print(moser_de_bruijn_numbers)