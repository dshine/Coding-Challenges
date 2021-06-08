import pytest
from handwash import wash_hands 

def test_handwash():
	"""Test paramaters
	"""
	assert wash_hands(8, 7) == "588 minutes and 0 seconds"
	assert wash_hands(0, 0) == "0 minutes and 0 seconds"
	assert wash_hands(7, 9) == "661 minutes and 30 seconds"
