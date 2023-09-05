def merge_list(input_list_1, input_list_2):
    output_list = [];
    for num in input_list_1:
        if (num % 2 == 1):
            output_list.append(num)
    for num in input_list_2:
        if (num % 2 == 0):
            output_list.append(num)
    return output_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))