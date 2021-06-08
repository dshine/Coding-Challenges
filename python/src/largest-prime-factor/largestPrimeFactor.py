__pdoc__ = {'main': False}

def largestPrimeFactor(num):
	""" 
	Takes 2 paramaters and caluclates the total of the numbers between the paramaters that are divisable by 3 or 5. 
	
	**param1** min  
	**param2** max  

	Returns the total

	"""
	i = 2
	largestPrime = 2 
	while i < num:
		if num % i == 0:
			largestPrime = i
			print(largestPrime)
		i = i + 1
	return largestPrime

def main():
	x = 600851475143
	x=13195
	answer = largestPrimeFactor(x)
	print(f"The largest prime factor of {x} is {answer}")

if __name__ == '__main__':
	main()