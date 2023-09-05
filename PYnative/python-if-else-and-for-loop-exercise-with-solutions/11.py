# range
start_num = 25
end_num = 50

is_prime_dict = {}
is_prime_dict[0] = False
is_prime_dict[1] = False
is_prime_dict[2] = True
is_prime_dict[3] = True
for i in range(1, (end_num*end_num)+1):
    num_i = i+1
    is_prime_dict[num_i] = True

for i in range(1, end_num + 1):
    num_i = i + 1
    for j in range(1, end_num + 1):
        num_j = j + 1
        is_prime_dict[num_i * num_j] = False

for i in range(start_num, end_num + 1):
    if (is_prime_dict[i+1]):
        print(i+1)