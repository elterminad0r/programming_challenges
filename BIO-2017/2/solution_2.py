#!/usr/bin/env python3.6

# Izaak van Dongen Hills Road Sixth Form College
# Solution to 2) a

"""
Reads input from stdin
"""

print("Izaak van Dongen HRSFC")

import string
from collections import deque

# hurts my soul but it works
# probably quadratic or something in the size of the alphabet but that's a
# constant so it's alright
def get_letters(n):
    circ = list(string.ascii_uppercase)
    sec = []
    pos = 0
    while circ:
        pos = (pos + n - 1) % len(circ)
        sec.append(circ.pop(pos))
    return "".join(sec)

def encrypt(word, n, dial):
    out = []
    for ch in word:
        out.append(dial[ord(ch.upper()) - 65])
        # more expressive than tracking offset + modulo
        dial.rotate(-1)
    return "".join(out)

n, word = input().split()
n = int(n)

dial = get_letters(n)

print(dial[:6])
print(encrypt(word, n, deque(dial)))
