COUNT_NUMS = 12

nc_nums_dict = {}
nc_nums_dict[0] = None
nc_nums_dict[1] = 1
nc_nums_dict[2] = 1

# newman_conway_numbers(n, nc_nums_dict)
# using "Dynamic Algorithm"
def nc_nums_seq(n, nc_nums_dict):
    if (n in nc_nums_dict.keys()):
        return nc_nums_dict[n]
    else:
        curr_num = nc_nums_seq(nc_nums_seq(n-1, nc_nums_dict), nc_nums_dict) + nc_nums_seq(n - nc_nums_seq(n-1, nc_nums_dict), nc_nums_dict)

        nc_nums_dict[n] = curr_num
        return curr_num

for n in range(1, COUNT_NUMS+1):
    print (nc_nums_seq(n, nc_nums_dict), end = ' ')