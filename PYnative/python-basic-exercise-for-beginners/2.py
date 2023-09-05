num = 10
curr_num = prev_num = 0
while (curr_num < num):
    print('Current Number ' + str(curr_num) + ' Previous Number  ' + str(prev_num) + ' Sum: ' + str(curr_num + prev_num))
    prev_num = curr_num
    curr_num += 1