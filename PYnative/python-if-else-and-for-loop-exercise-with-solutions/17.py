length = 5
digit = 2
sum = 0
addition_list = [];
for l in range(1, length+1):
    sum += int(str(digit)*l)
    addition_list.append(str(digit)*l)
print('+'.join(addition_list), '=', sum)