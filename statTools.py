def find_range(array):
    try:
        lenArr = len(array)
        if lenArr > 0:
            array = merge_sort(array)
            array_range = array[lenArr-1] - array[0]
        else:
            return 0
        return array_range
    except:
        return -1

def lower_quartile(array):
    return 0



def merge(array1, array2):
    array = []
    lenArr1 = len(array1)
    lenArr2 = len(array2)
    i1 = 0
    i2 = 0

    while i1 < lenArr1 and i2 < lenArr2:
        if array1[i1] < array2[i2]:
            array.append(array1[i1])
            i1 += 1
        else:
            array.append(array2[i2])
            i2 += 1
    while i1 < lenArr1:
        array.append(array1[i1])
        i1 += 1
    while i2 < lenArr2:
        array.append(array2[i2])
        i2 += 1

    return array

def merge_sort(array):
    lenArr = len(array)
    mid = int(lenArr/2)
    if lenArr <= 1:
        return array
    else:
        return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))