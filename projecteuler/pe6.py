#===============================================================================
# Project Euler: Problem 6 - Sum square difference
#
# __author__ = "Zenith"
# __copyright__ = "Copyright 2013 by RockStone"
# __license__ = "GPL"
# __email__ = "zenith at rockstone dot me"
#===============================================================================

def sum_square_difference(n):
	sum = sum_of_squares = 0
	for i in range(n + 1):
		sum_of_squares += i ** 2
		sum += i
	square_of_sum = sum ** 2
	return square_of_sum - sum_of_squares

if __name__ == "__main__":
	print(sum_square_difference(100))
