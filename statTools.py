"""
-------------------------------------------------------------------------------
Name:   statTools.py
Purpose:
Create functions that help with statistical analysis

Author:   hartanovich.t and sumi.j

Created:    11/11/2018
------------------------------------------------------------------------------
"""


''' find_range
A function that finds the range of a given set of values
:param array: integer array of values
:return: int  the difference between greatest and smallest value
'''
def find_range(array):
    try:
        lenArr = len(array)
        if lenArr > 0:
            array = merge_sort(array)
            return array[lenArr-1] - array[0]
        else:
            return 0
    except:
        return "error"

''' lower_quartile
A function that finds the median of the lower half of a set of values
:param array: integer array of values
:return: int  the median of the lower half of the array
'''
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

''' upper_quartile
A function that finds the median of the upper half of a set of values
:param array: integer array of values
:return: int  the median of the upper half of the array
'''
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

''' variance
A function that finds the difference between every value compared to the mean, squares it and returns the mean of 
the resulting set of numbers
:param array: integer array of values
:return: int  the mean of the squared values of the differences between the numbers and the mean
'''
def variance(array):
    try:
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
    except:
        return "error"

''' standard_deviation
A function that finds the square root of the variance
:param array: integer array of values
:return: int  the root of the variance rounded to 2 decimals
'''
def standard_deviation(array):
    try:
        return round(variance(array)**0.5,2)
    except:
        return "error"


''' merge
Merges two sorted arrays into 1 big one
:param array1: first sorted integer array of values
:param array2: second sorted integer array of values
:return: int[] a sorted final array
'''
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

''' merge_sort
Sorts an array from least to greatest
:param array: sorts an array from least to greatest
:return: int[] the sorted array
'''
def merge_sort(array):
    lenArr = len(array)
    mid = int(lenArr/2)
    if lenArr <= 1:
        return array
    else:
        return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))