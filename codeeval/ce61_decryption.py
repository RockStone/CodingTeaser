#!/usr/bin/python

# __author__ = "Zenith"
# __email__ = "zenith @ rockstone . me"

import re
import sys

def decryption(msg, key):
    word = msg.split()
    for w in word:
        sys.stdout.write(''.join(map(lambda code: chr(key.index(chr(code + 65)) + 65),
                  map(int, re.findall('..', w)))) + " ")

msg = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119"
key = "BHISOECRTMGWYVALUZDNFJKPQX"

decryption(msg, key)
