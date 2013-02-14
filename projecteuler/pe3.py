#===============================================================================
# Project Euler: Problem 3 - Largest prime factor
#
# __author__ = "Zenith"
# __copyright__ = "Copyright 2013 by RockStone"
# __license__ = "GPL"
# __email__ = "zenith at rockstone dot me"
#===============================================================================

import math
from time import time

def pe3v1(n):
	divisor = 2
	while divisor <= int(n**0.5 + 1):
		while (n % divisor) == 0:
			n //= divisor
		divisor += 1
	if n > 1: return n
	else:
		return divisor - 1

def pe3v2(n):
	m, d, i = 1, 0, 2
	for i in xrange(2, int(n**0.5 + 1)):
		if n % i == 0:
			if m * i > n:
				return d
			else:
				m *= i
				d = i

if __name__ == "__main__":
	 t0 = time()
	 print(pe3v1(600851475143))
	 t1 = time()
	 print 'pe3v1: %f' %(t1 - t0)
	 print(pe3v2(600851475143))
	 t2 = time()
	 print 'pe3v2: %f' %(t2 - t1)
