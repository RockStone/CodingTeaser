#!/usr/bin/python
"""
Discount Offer program to find maximum Suitability Score for Product-Customer pairs.
Reference: http://www.public.iastate.edu/~ddoty/HungarianAlgorithm.html
Disclaimer: Please be advised this program is displayed for study purpose ONLY.
            You may NOT use it for job application or other commercial interests.
            Distribution of this program is NOT allowed without the author's expressive consent.
"""
# __author__ = "Zenith"
# __email__ = "zenith @ rockstone . me"

from re import sub
from sys import argv
from sys import maxint

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def countVowels(s):
    vowels = 'aeiouy'
    return len([c for c in s if c in vowels])

def suitabilityMx(cuspro):
    cusname, proname = cuspro.split(";")
    cusname = cusname.split(",")
    proname = proname.split(",")
    cus, pro = [], []

    for s in cusname:
        a, b = len(s), countVowels(s)
        cus.append([a, b, a - b])

    for s in proname:
        pro.append(len(s))

    lc, lp = len(cus), len(pro)
    mx = [[[] for _ in xrange(lc)] for _ in xrange(lp)]
    i, j = [0] * 2

    for p in pro:
        for c in cus:
            if p % 2 == 0: mx[i][j] = c[1] * 1.5
            else: mx[i][j] = c[2]
            if gcd(p, c[0]) > 1: mx[i][j] *= 1.5
            j += 1
        j = 0
        i += 1
    return mx

def computeMaxSum(mx):
    row = []
    lc, lp = len(mx[0]), len(mx)
    memo = [False for _ in xrange(lc)]
    rank = [[[] for _ in xrange(lc)] for _ in xrange(lp)]

    for i in xrange(lp):
        for j in xrange(lc):
            row.append(mx[i][j])
        row.sort()
        for j in xrange(lc):
            if row.index(mx[i][j]) >= (lc - lp): rank[i][j] = True
            else: rank[i][j] = False

    maxsum = [-maxint - 1]

    def rec(i, sum):
        if i == lp:
            if sum > maxsum[0]: maxsum[0] = sum
            return
        for j in xrange(lc):
            if not memo[j] and rank[i][j]:
                memo[j] = True
                rec(i + 1, sum + mx[i][j]) # bad algorithm!!! fail!!!
                memo[j] = False
    rec(0, 0)
    return maxsum[0]

if __name__ == "__main__":
    file = argv[1]
    with open(file) as fh:
        lines = [sub("[~!@#$%^&*()_+={}<>:\.\-\d\s]", "", _.lower()) for _ in fh]
    for cuspro in lines:
        smx = suitabilityMx(cuspro)
        maxsum = computeMaxSum(smx)
        print "%.2f" % float(maxsum)
