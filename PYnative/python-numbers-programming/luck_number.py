start_num   = 1
end_num     = 327

luck_numbers = list(range(start_num,end_num+1))[::2]
i = 1
remove_index = luck_numbers[i]
while(remove_index < len(luck_numbers)):
    removed_nums = luck_numbers[remove_index-1::remove_index]

    for r_num in removed_nums:
        luck_numbers.remove(r_num)
    
    i += 1 
    remove_index = luck_numbers[i]   

print(luck_numbers)