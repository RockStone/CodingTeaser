#===============================================================================
# Project Euler: Problem 2 - Even Fibonacci numbers
#
# __author__ = "Zenith"
# __copyright__ = "Copyright 2013 by RockStone"
# __license__ = "GPL"
# __email__ = "zenith at rockstone dot me"
#===============================================================================

def pe2v1(r, f0 = 1, f1 = 2):
	f2 = f1
	sum = 0
	while f2 < r:
		if f2 % 2 == 0:
			sum += f2
		f2 = f0 + f1
		f0 = f1
		f1 = f2
	return sum

def pe2v2(r, seq = [1, 2]):
	while seq[-1] < r:
		seq.append(seq[-1] + seq[-2])
	return sum(seq[1::3])

if __name__ == "__main__":
	print(pe2v1(4000000))
	print(pe2v2(4000000))
