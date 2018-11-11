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
        len_arr = len(array)

        # Check if the length of the array is greater than 1
        if len_arr > 1:

            # Sort the array and return the difference between highest and lowest number
            array = merge_sort(array)
            return array[len_arr - 1] - array[0]
        else:
            # If the arrays length is less than 2 the difference between highest and lowest will be 0
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
        len_arr = len(array)
        if len_arr > 0:
            # get the lower half of the array
            top_val = int((len_arr + 1) / 2)
            array = merge_sort(array)
            array = array[:top_val]

            mid = int(top_val / 2)

            # find the median
            if top_val % 2 == 0:
                return (array[mid - 1] + array[mid]) / 2
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
        len_arr = len(array)
        if len_arr > 0:
            # get the upper half of the array
            min_val = int(len_arr / 2)
            array = merge_sort(array)
            array = array[min_val:]

            mid = int(min_val / 2)

            # find the median
            if (len_arr - min_val) % 2 == 0:
                return (array[mid + 1] + array[mid]) / 2
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
        len_arr = len(array)
        if len_arr > 0:
            mean = 0
            variance_out = 0

            # find mean
            for i in range(len_arr):
                mean += array[i]
            mean /= len_arr

            # find difference between every number and the mean, square it, then add it to the total
            for i in range(len_arr):
                variance_out += (array[i] - mean) ** 2
            variance_out /= len_arr

            return variance_out
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
        return round(variance(array) ** 0.5, 2)
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
    len_arr1 = len(array1)
    len_arr2 = len(array2)
    i1 = 0
    i2 = 0

    while i1 < len_arr1 and i2 < len_arr2:
        if array1[i1] < array2[i2]:
            array.append(array1[i1])
            i1 += 1
        else:
            array.append(array2[i2])
            i2 += 1
    while i1 < len_arr1:
        array.append(array1[i1])
        i1 += 1
    while i2 < len_arr2:
        array.append(array2[i2])
        i2 += 1

    return array


''' merge_sort
Sorts an array from least to greatest
:param array: sorts an array from least to greatest
:return: int[] the sorted array
'''


def merge_sort(array):
    len_arr = len(array)
    mid = int(len_arr / 2)
    if len_arr <= 1:
        return array
    else:
        return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))
