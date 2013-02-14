#===============================================================================
# Project Euler: Problem 5 - Smallest multiple
#
# __author__ = "Zenith"
# __copyright__ = "Copyright 2013 by RockStone"
# __license__ = "GPL"
# __email__ = "zenith at rockstone dot me"
#===============================================================================

from time import time

def gcd(a, b):
	while (b != 0):
		a, b = b, a % b
	return a

def factorize(n):
	factor = {}

	if n == 1: return {1:1}
	else:
		divisor = 2
		while divisor <= n:
			power = 0
			while (n % divisor) == 0:
				n //= divisor
				power += 1
			if power > 0:
				factor.update({divisor: power}) # factor[divisor] = power
			divisor += 1
		if n > 1:
			factor.update({divisor: power})
		return factor

def maxfactorize(m):
	maxfactor = {}
	for i in xrange(1, m):
		factor = factorize(i)
		for key, value in factor.iteritems():
			if maxfactor.get(key) is None: maxfactor.update({key: value})
			elif maxfactor.get(key) < value: maxfactor.update({key: value})
	return maxfactor

def pe5_factorization(num):
	maxfactor = maxfactorize(num)
	product = 1
	for key, value in maxfactor.iteritems():
		product *= key ** value
	return product

def pe5_iteration(num):
	start = 1
	for i in xrange(1, num):
		start *= i / gcd(i, start) # LCM
	return start

if __name__ == "__main__":
	num = 21
	t0 = time()
	print(pe5_factorization(num))
	t1 = time()
	print "%.20f" % (t1 - t0)

	print(pe5_iteration(num))
	t2 = time()
	print "%.20f" % (t2 - t1)