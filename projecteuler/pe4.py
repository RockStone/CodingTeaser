#===============================================================================
# Project Euler: Problem 4 - Largest palindrome product
#
# __author__ = "Zenith"
# __copyright__ = "Copyright 2013 by RockStone"
# __license__ = "GPL"
# __email__ = "zenith at rockstone dot me"
#===============================================================================

import itertools
from time import time

def ispalindrome_v1(n):
	d = []
	while (n > 0):
		d.append(n % 10)
		n //= 10
	for i in range(len(d) / 2):
		if (d[i] != d[-(i + 1)]):
			return False
	return True

def ispalindrome_v2(n):
	return str(n) == str(n)[::-1]

def bruteforce_v1():
	perm = list(itertools.permutations(range(1000, 100, -1), 2))
	palin = 0
	for i in range(len(perm)):
		n = perm[i][0] * perm[i][1]
		if (str(n) == str(n)[::-1]) and (palin < n): palin = n
	if (palin): return palin
	else: return "No palindromic number found!"

def bruteforce_v2():
	palin = 0
	i = 999
	j = 990
	while (i > 100):
		j = 990
		while (j > 100):
			n = i * j
			if (palin < n) and (str(n) == str(n)[::-1]): palin = n
			j -= 11
		i -= 1
	return palin

if __name__ == "__main__":
	t0 = time()
	print bruteforce_v1()
	t1 = time()
	print t1 - t0
	print bruteforce_v2()
	t2 = time()
	print t2 - t1

