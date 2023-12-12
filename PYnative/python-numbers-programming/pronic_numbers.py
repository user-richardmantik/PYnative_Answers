import math

def is_pronic(num):
    n = math.floor(math.sqrt(num))
    n_plus_one = n + 1

    return num == n * n_plus_one

start_num   = 0
end_num     = 500

pronic_numbers = list()
for num_i in range (start_num, end_num + 1):
    if (is_pronic(num_i)):
        pronic_numbers.append(num_i)

print (', '.join([str(num) for num in pronic_numbers]))