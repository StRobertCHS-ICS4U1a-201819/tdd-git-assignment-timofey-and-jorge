import pytest
from statTools import *

def test_mean_empty():
    assert(mean([]) == 0)