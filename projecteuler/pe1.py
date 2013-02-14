#===============================================================================
# Project Euler: Problem 1 - Multiples of 3 and 5
#
# __author__ = "Zenith"
# __copyright__ = "Copyright 2013 by RockStone"
# __license__ = "GPL"
# __email__ = "zenith at rockstone dot me"
#===============================================================================

def pe1v1(r):
	sum = 0
	for i in range(r):
		if(i % 3 == 0 or i % 5 == 0):
			sum += i
	return sum

def pe1v2(r):
	return sum(set(range(3, r, 3) + range(5, r, 5)))

if __name__ == "__main__":
	print(pe1v1(10))
	print(pe1v2(10))
