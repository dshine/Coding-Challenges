import calc

def test_totals():
	assert calc.sum_range_multiples_3_5(1,10) == 23
	assert calc.sum_range_multiples_3_5(1,100) == 2318
	assert calc.sum_range_multiples_3_5(1,1000) == 233168
