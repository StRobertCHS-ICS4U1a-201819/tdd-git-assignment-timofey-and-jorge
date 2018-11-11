import pytest
from statTools import *

def test_find_range_basic():
    assert(find_range([1,2,3,4,5]) == 4)

def test_find_range_unsorted():
    assert(find_range([3,2,4,1,5]) == 4)

def test_find_range_empty():
    assert(find_range([]) == 0)

def test_find_range_negative():
    assert(find_range([1,2,3,4,100,-26,-73,-100]) == 200)

def test_find_range_non_array():
    assert(find_range("no") == -1)

def test_merge_basic():
    assert(merge([1,3,5,7,9],[2,4,6,8,10]) == [1,2,3,4,5,6,7,8,9,10])

def test_merge_sort_basic():
    assert(merge_sort([5,2,7,4,8,3,9,1,6]) == [1,2,3,4,5,6,7,8,9])

def test_merge_sort_repeated():
    assert(merge_sort([5,2,7,3,8,2,9,3,5,3,5,3]) == [2,2,3,3,3,3,5,5,5,7,8,9])
