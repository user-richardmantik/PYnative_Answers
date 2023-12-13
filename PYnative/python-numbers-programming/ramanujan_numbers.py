import time
import math

start_num = 1
end_num = 100000

start_time = time.time()

ramanujan_dict = {}

for num_i in range(1, math.ceil(math.pow(end_num, 1/3)) + 1):
    for num_j in range (num_i + 1, math.ceil(math.pow(end_num, 1/3)) + 1):
        sum_2_cubes = num_i ** 3 + num_j ** 3
        if (sum_2_cubes not in ramanujan_dict.keys()):
            ramanujan_dict[sum_2_cubes] = []
        ramanujan_dict[sum_2_cubes].append((num_i, num_j))

for sum_2_cubes, pairs in ramanujan_dict.items():
    ramanujan_pairs_list = ramanujan_dict[sum_2_cubes]
    if (len(ramanujan_pairs_list) > 1):
        print(sum_2_cubes, end='')
        for ramanujan_pair in ramanujan_pairs_list:
            print(' = ' + str(ramanujan_pair[0]) + '^3 + ' + str(ramanujan_pair[1]) + '^3', end='')
        print()

end_time = time.time()

print("The time of execution of above program is :", (end_time-start_time) * 10**3, "ms")