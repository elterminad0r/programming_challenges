#!/usr/bin/env python3.6

# Izaak van Dongen Hills Road Sixth Form College
# Solution to 3) a

print("Izaak van Dongen HRSFC")

import itertools

def gen_equivalents(ser, encountered, depth=1):
    for i in range(len(ser) - 1):
        j = i + 1
        for k in (i - 1, i + 2):
            if 0 <= k < len(ser) and 1 in map(abs, [k - i, k - j]):
                iv, jv = sorted([ser[i], ser[j]])
                if iv < ser[k] < jv:
                    sercpy = list(ser)
                    sercpy[i], sercpy[j] = sercpy[j], sercpy[i]
                    mutser = tuple(sercpy)

                    if mutser in encountered:
                        if encountered[mutser] > depth:
                            encountered[mutser] = depth
                            gen_equivalents(mutser, encountered, depth + 1)
                    else:
                        encountered[mutser] = depth
                        gen_equivalents(mutser, encountered, depth + 1)

    return encountered

if __name__ == "__main__":
    size = input()
    serial = input()

    print(max(gen_equivalents(serial, {}).values()))
