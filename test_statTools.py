import pytest
from statTools import *

def test_find_range_basic():
    assert(find_range([1,2,3,4,5]) == 4)

def test_find_range_unsorted():
    assert(find_range([3,2,4,1,5]) == 4)

def test_merge_basic():
    assert(merge([1,3,5,7,9],[2,4,6,8,10]) == [1,2,3,4,5,6,7,8,9,10])
