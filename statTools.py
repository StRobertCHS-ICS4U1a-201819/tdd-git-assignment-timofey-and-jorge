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
        return "error"

def lower_quartile(array):
    try:
        lenArr = len(array)
        if lenArr > 0:
            topVal = int((lenArr + 1) / 2)
            array = merge_sort(array)
            array = array[:topVal]

            mid = int(topVal/2)

            if (topVal % 2 == 0):
                return (array[mid-1]+array[mid]) / 2
            return array[mid] / 1
        else:
            return 0
    except:
        return "error"

def upper_quartile(array):
    try:
        lenArr = len(array)
        if lenArr > 0:
            minVal = int((lenArr) / 2)
            array = merge_sort(array)
            array = array[minVal:]

            mid = int(minVal/2)

            if ((lenArr-minVal) % 2 == 0):
                return (array[mid+1]+array[mid]) / 2
            return array[mid] / 1
        else:
            return 0
    except:
        return "error"

def variance(array):
    lenArr = len(array)
    if lenArr > 0:
        mean = 0
        variance = 0

        for i in range(lenArr):
            mean += array[i]
        mean /= lenArr

        for i in range(lenArr):
            variance += (array[i] - mean)**2
        variance /= lenArr

        return variance
    else:
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