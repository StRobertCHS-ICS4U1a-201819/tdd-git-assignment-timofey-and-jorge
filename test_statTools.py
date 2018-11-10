import pytest
from statTools import *

def test_find_range_basic():
    assert(find_range([1,2,3,4,5]) == 4)

