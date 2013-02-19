#!/usr/bin/python
"""
Disclaimer: Please be advised this program is displayed for study purpose ONLY.
            You may NOT use it for job application or other commercial interests.
            Distribution of this program is NOT allowed without the author's expressive consent.
"""
# __author__ = "Zenith"
# __email__ = "zenith @ rockstone . me"

import sys

def fizzbuzz(buzz):
   fb = []
   for i in range(1, buzz[2] + 1):
       if i % buzz[0] == 0 and i % buzz[1] == 0:
           fb.append('FB')
       elif i % buzz[0] == 0:
           fb.append('F')
       elif i % buzz[1] == 0:
           fb.append('B')
       else:
           fb.append(i)
   return fb

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as fh:
        fizz = [map(int, line.split()) for line in fh]
    for buzz in fizz:
        print " ".join(map(str, fizzbuzz(buzz)))

fh.close()
