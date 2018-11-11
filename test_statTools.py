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
    assert(find_range("no") == "error")

def test_lower_quartile_basic():
    assert(lower_quartile([1,2,3,4,5,6]) == 2)

def test_lower_quartile_odd():
    assert(lower_quartile([1,2,3,4,5,6,7]) == 2.5)

def test_lower_quartile_empty():
    assert(lower_quartile([]) == 0)

def test_lower_quartile_unsorted():
    assert(lower_quartile([7,4,6,5,1,3,2]) == 2.5)

def test_lower_quartile_negative():
    assert(lower_quartile([-3,3,-2,2,-1,1,0]) == -1.5)

def test_lower_quartile_non_array():
    assert(lower_quartile("no") == "error")

def test_upper_quartile_basic():
    assert(upper_quartile([1,2,3,4,5,6]) == 5)

def test_upper_quartile_odd():
    assert(upper_quartile([1,2,3,4,5,6,7]) == 5.5)

def test_upper_quartile_empty():
    assert(upper_quartile([]) == 0)

def test_upper_quartile_unsorted():
    assert(upper_quartile([7,4,6,5,1,3,2]) == 5.5)

def test_upper_quartile_negative():
    assert(upper_quartile([-3,3,-2,2,-1,1,0]) == 1.5)

def test_upper_quartile_non_array():
    assert(upper_quartile("no") == "error")



def test_merge_basic():
    assert(merge([1,3,5,7,9],[2,4,6,8,10]) == [1,2,3,4,5,6,7,8,9,10])

def test_merge_sort_basic():
    assert(merge_sort([5,2,7,4,8,3,9,1,6]) == [1,2,3,4,5,6,7,8,9])

def test_merge_sort_repeated():
    assert(merge_sort([5,2,7,3,8,2,9,3,5,3,5,3]) == [2,2,3,3,3,3,5,5,5,7,8,9])
