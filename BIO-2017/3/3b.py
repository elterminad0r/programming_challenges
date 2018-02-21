#!/usr/bin/env python3.6

# Izaak van Dongen Hills Road Sixth Form College
# Script used to help answer 3) b

print("Izaak van Dongen HRSFC")

import itertools
import sys

from solution_3 import gen_equivalents

poss = gen_equivalents(sys.argv[1], {})

best = 0
bfrom = "init"
bto = "init"

for k in map("".join, itertools.chain(poss.keys(), ["326451"])):
    to, mv = max(list(gen_equivalents(k, {}).items()), key=lambda x: x[1])
    print("equivalent is {} - max is {}".format(k, mv))
    if mv > best:
        best = mv
        bfrom = k
        bto = to

print(best, bfrom, "".join(bto))
