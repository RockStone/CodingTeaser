#!/usr/bin/python
"""
Disclaimer: Please be advised this program is displayed for study purpose ONLY.
            You may NOT use it for job application or other commercial interests.
            Distribution of this program is NOT allowed without the author's expressive consent.
"""
# __author__ = "Zenith"
# __email__ = "zenith @ rockstone . me"

import sys

def isPrime(n):
    if n <= 1: raise "n must be greater than 1" 
    if n == 2: return True
    else:
        for i in range(2, int(n**0.5 + 1)):
            if n % i == 0: return False
    return True

file = sys.argv[1]

with open(file) as fh:
    n = map(int, fh)

for m in n:
   for i in range(2, m):
       if isPrime(i):
           if i > 2: sys.stdout.write(",")
           sys.stdout.write("%d" % i)
   sys.stdout.write("\r")
   sys.stdout.flush()
