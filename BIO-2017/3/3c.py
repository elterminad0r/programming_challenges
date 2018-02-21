#!/usr/bin/env pypy

# Izaak van Dongen Hills Road Sixth Form College
# Script used to help answer 3) c
# Run with PyPy

print("Izaak van Dongen HRSFC")

import itertools
import sys
import string

from solution_3 import gen_equivalents

n = int(sys.argv[1])
tc = string.digits[1: n + 1]

print("testing {} ({})".format(n, tc))

best = 0

accounted = set()

for test, i in zip(itertools.permutations(tc), itertools.count()):
    if test not in accounted:
        if i % 100 == 0:
            print("\r{}".format(test), end="")
        eq = gen_equivalents(test, {})
        accounted.update(eq)
        l = len(eq)
        if l > best:
            print("\r{} ups to {}".format(test, l))
            best = l

print("\r{}".format(" " * 80))
