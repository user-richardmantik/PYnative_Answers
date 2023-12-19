import random
import math

def merge_sort(array):
    if (len(array) > 1):
        mid_index = math.ceil(len(array) / 2)

        left_array  = array[0:mid_index]
        right_array = array[mid_index:len(array)]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0
        while (i < len(left_array) and j < len(right_array)):
            if (left_array[i] < right_array[j]):
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while (i < len(left_array)):
            array[k] = left_array[i]
            i+=1 
            k+=1
        while (j < len(right_array)):
            array[k] = right_array[j]
            j+=1
            k+=1


count_bugs = 0
for i in range (1, 1000000+1):
    array = [
        random.randint(3, 9)
        , random.randint(3, 9)
        , random.randint(3, 9)
        , random.randint(3, 9)
        , random.randint(3, 9)
        , random.randint(3, 9)
        , random.randint(3, 9)
        , random.randint(3, 9)
        , random.randint(3, 9)]
    merge_sort(array)
    if (array != sorted(array)):
        count_bugs += 1

print(count_bugs)
