# Project Description

If we list all the numbers between 1 and 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. Add those numbers together and you get 23.

Write a function that finds the sum of all the numbers between X and Y that are multiples of 3 or 5. 

## Psudeo code
```
calc_function(X,Y)
	total = 0
	for i between X and Y
		if i % 3 or i % 5 is zero
			total = total + i
	return total 
```
## Tests
```
	assert sum_range_multiples_3_5(1,10) == 23
	assert sum_range_multiples_3_5(1,100) == 2318
	assert sum_range_multiples_3_5(1,1000) == 233168
```

