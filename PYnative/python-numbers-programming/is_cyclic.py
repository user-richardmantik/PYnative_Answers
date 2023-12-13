import math

def count_digits(num): 
    return math.floor(math.log10(num)+1)

def get_cyclic_permutations(N):
    cyclic_permutations = []
    num = N
    n = count_digits(N)
    while (1):
        cyclic_permutations.append(int(num))
        rem = num % 10
        div = math.floor(num / 10)
        num = ((math.pow(10, n - 1)) * rem + div)
        if (num == N):
            break

    return cyclic_permutations

def is_cyclic(num):
    cyclic_permutations = sorted(get_cyclic_permutations(num))
    is_cyclic = True
    for n in (1, count_digits(num)):
        if ((n * num) not in cyclic_permutations):
            is_cyclic = False

    return is_cyclic

num = int(input('Input a number: '))
if (is_cyclic(num)):
    print (num, 'is a cyclic number.')
else:
    print (num, 'is NOT a cyclic number.')