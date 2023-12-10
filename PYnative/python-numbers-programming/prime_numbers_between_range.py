import math

start_num = 1
end_num = 1000

is_prime_dict = {}
is_prime_dict[0] = False
is_prime_dict[1] = False

count_primes = 0
sum_primes = 0
for i in range(1, end_num):
    num_i = i+1
    is_prime_dict[num_i] = True

for num_i in range(2, math.ceil(end_num/2)):
    for num_j in range(num_i, math.ceil(end_num/2)):
        is_prime_dict[num_i * num_j] = False

for num_i in range(start_num, end_num+1):
    if (is_prime_dict[num_i]):
        print(num_i)
        count_primes += 1
        sum_primes += num_i

print('count_primes =', count_primes)
print('sum_primes =', sum_primes)