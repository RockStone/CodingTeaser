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

class Hungarian:
    def __init__(self):
        self.rowmem, self.colmem = [[]] * 2
        self.n, self.zrow, self.zcol = [0] * 3
        self.shadow, self.tagged, self.path = [None] * 3

    def alterPath(self, path, count):
        for i in range(count + 1):
            if self.tagged[path[i][0]][path[i][1]] == 1:
                self.tagged[path[i][0]][path[i][1]] = 0
            else:
                self.tagged[path[i][0]][path[i][1]] = 1

    def createMx(self, n, val):
        mx = []
        for i in range(n):
            mx += [[val for j in range(n)]]
        return mx

    def computeMx(self, pmx):
        self.shadow = self.padMx(pmx)
        self.n = len(self.shadow)
        self.leninit, self.widinit = len(pmx), len(pmx[0])
        self.rowmem = [False for i in range(self.n)]
        self.colmem = [False for i in range(self.n)]
        self.zrow, self.zcol = [0] * 2
        self.path, self.tagged = self.createMx(self.n * 2, 0), self.createMx(self.n, 0)
        done = False
        step = 1
        steps = { 1 : self.s1,
                  2 : self.s2,
                  3 : self.s3,
                  4 : self.s4,
                  5 : self.s5,
                  6 : self.s6 }
        while not done:
            try:
                func = steps[step]
                step = func()
            except KeyError:
                done = True
        results = []
        for i in range(self.leninit):
            for j in range(self.widinit):
                if self.tagged[i][j] == 1:
                    results += [(i, j)]
        return results

    def flushMem(self):
        for i in range(self.n):
            self.rowmem[i], self.colmem[i] = [False] * 2

    def flushPrime(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.tagged[i][j] == 2:
                    self.tagged[i][j] = 0

    def padMx(self, mx, padval = 0):
        maxcol, totrow = 0, len(mx)
        for row in mx:
            maxcol = max(maxcol, len(row))
        totrow, nmx = max(maxcol, totrow), []
        for row in mx:
            rowlen, nrow = len(row), row[:]
            if totrow > rowlen:
                nrow += [0] * (totrow - rowlen)
            nmx += [nrow]
        while len(nmx) < totrow:
            nmx += [[0] * totrow]
        return nmx
    
    def searchColTag(self, col):
        row = -1
        for i in range(self.n):
            if self.tagged[i][col] == 1:
                row = i
                break
        return row

    def searchRowTag(self, row):
        col = -1
        for j in range(self.n):
            if self.tagged[row][j] == 1:
                col = j
                break
        return col

    def searchRowPrime(self, row):
        col = -1
        for j in range(self.n):
            if self.tagged[row][j] == 2:
                col = j
                break
        return col

    def searchZero(self):
        row, col = [-1] * 2
        i = 0
        n = self.n
        done = False
        while not done:
            j = 0
            while True:
                if (self.shadow[i][j] == 0) and \
                   (not self.rowmem[i]) and \
                   (not self.colmem[j]):
                    row, col = i, j
                    done = True
                j += 1
                if j >= n:
                    break
            i += 1
            if i >= n:
                done = True
        return (row, col)

    def s1(self):
        shadow, n = self.shadow, self.n
        for i in range(n):
            maxval = max(self.shadow[i])
            for j in range(n):
                self.shadow[i][j] += maxval
        return 2

    def s2(self):
        n = self.n
        for i in range(n):
            for j in range(n):
                if (self.shadow[i][j] == 0) and \
                   (not self.colmem[j]) and \
                   (not self.rowmem[i]):
                    self.tagged[i][j] = 1
                    self.colmem[j], self.rowmem[i] = [True] * 2
        self.flushMem()
        return 3

    def s3(self):
        n = self.n
        count = 0
        for i in range(n):
            for j in range(n):
                if self.tagged[i][j] == 1:
                    self.colmem[j] = True
                    count += 1
        if count >= n:
            step = 7
        else:
            step = 4
        return step

    def s4(self):
        step = 0
        done = False
        row, col, tagcol = [-1] * 3
        while not done:
            (row, col) = self.searchZero()
            if row < 0:
                done = True
                step = 6
            else:
                self.tagged[row][col] = 2
                tagcol = self.searchRowTag(row)
                if tagcol >= 0:
                    col = tagcol
                    self.rowmem[row], self.colmem[col] = True, False
                else:
                    done = True
                    self.zrow, self.zcol = row, col
                    step = 5
        return step

    def s5(self):
        count = 0
        path = self.path
        path[count][0], path[count][1] = self.zrow, self.zcol
        done = False
        while not done:
            row = self.searchColTag(path[count][1])
            if row >= 0:
                count += 1
                path[count][0] = row
                path[count][1] = path[count - 1][1]
            else:
                done = True
            if not done:
                col = self.searchRowPrime(path[count][0])
                count += 1
                path[count][0] = path[count - 1][0]
                path[count][1] = col
        self.alterPath(path, count)
        self.flushMem()
        self.flushPrime()
        return 3

    def s6(self):
        maxval = self.returnMax()
        for i in range(self.n):
            for j in range(self.n):
                if self.rowmem[i]:
                    self.shadow[i][j] += maxval
                if not self.colmem[j]:
                    self.shadow[i][j] -= maxval
        return 4

    def returnMax(self):
        maxval = -maxint - 1
        for i in range(self.n):
            for j in range(self.n):
                if (not self.rowmem[i]) and (not self.colmem[j]):
                    if maxval < self.shadow[i][j]:
                        maxval = self.shadow[i][j]
        return maxval

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

if __name__ == "__main__":
    file = argv[1]
    with open(file) as fh:
        lines = [sub("[~!@#$%^&*()_+={}<>:\.\-\d\s]", "", _.lower()) for _ in fh]
    for cuspro in lines:
        smx = suitabilityMx(cuspro)
        hungarian = Hungarian()
        tagmx = hungarian.computeMx(smx)
        maxsum = 0.
        for row, col in tagmx:
            maxsum += smx[row][col]
        print '%.2f' % maxsum
