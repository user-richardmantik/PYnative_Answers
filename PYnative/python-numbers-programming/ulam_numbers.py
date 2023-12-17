COUNT_NUMS = 27

ulam_nums = [1, 2]

last_num = 2
count_ulam_nums = 2
while (count_ulam_nums < COUNT_NUMS):
    maybe_ulam_num = last_num + 1
    
    count_combs = 0
    for i in range(0, len(ulam_nums)):
        for j in range(i + 1, len(ulam_nums)):
            if (ulam_nums[i]+ulam_nums[j] == maybe_ulam_num):
                count_combs += 1
    
    if (count_combs == 1):
        ulam_nums.append(maybe_ulam_num) 

        count_ulam_nums += 1
    last_num += 1
    

print(ulam_nums)