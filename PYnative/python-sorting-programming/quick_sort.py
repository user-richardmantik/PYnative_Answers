import random
def quick_sort(array, low_index, high_index):

    if (low_index >= high_index): return
    pivot = array[low_index]

    i = low_index + 1
    j = high_index
    
    while (True):
        while(i <= j and array[i] <= pivot):
            i += 1
        while(i <= j and array[j] >= pivot):
            j -= 1
        
        if (i <= j):
            (array[i], array[j]) = (array[j], array[i])
        else:
            break

    (array[j], array[low_index]) = (array[low_index], array[j])
    
    quick_sort(array, low_index, j-1)
    quick_sort(array, i, high_index)


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
    quick_sort(array, 0, len(array) - 1)
    if (array != sorted(array)):
        count_bugs += 1

print(count_bugs)