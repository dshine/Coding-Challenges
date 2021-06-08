import pytest
from calc import sum_range_multiples_3_5 

def test_totals():
	assert sum_range_multiples_3_5(1,10) == 23
	assert sum_range_multiples_3_5(1,100) == 2318
	assert sum_range_multiples_3_5(1,1000) == 233168
