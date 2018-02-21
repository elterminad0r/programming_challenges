#!/usr/bin/env python3.6

# Izaak van Dongen Hills Road Sixth Form College
# Solution to 1) a

"""
Reads input from stdin. Call without argv for behaviour as specified.
"""

print("Izaak van Dongen HRSFC")

import itertools
import sys

DEBUG = "debug" in map(str.lower, sys.argv)

def _print(s):
    if DEBUG:
        print(s)

# percentage rounding upwards
def get_percentage(dbt, perc):
    return -((-dbt * perc) // 100)

def mformat(money):
    smoney = str(money)
    pounds, pennies = smoney[:-2], smoney[-2:].rstrip("0")
    if pennies:
        return "{}.{}".format(pounds, pennies)
    else:
        return pounds

def run_debt(debt, p_interest, p_repayment):
    sum_repaid = 0

    for month in itertools.count(1):
        _print("\nmonth {}: debt is {:.2f}".format(month, debt / 100))
        interest = get_percentage(debt, p_interest)
        _print("interest {:.2f}".format(interest / 100))
        debt += interest
        _print("debt increased to {:.2f}".format(debt / 100))

        repayment = min(debt, max(5000, get_percentage(debt, p_repayment)))
        _print("must repay {:.2f}".format(repayment / 100))
        debt -= repayment
        sum_repaid += repayment
        _print("debt decreased to {:.2f}".format(debt / 100))

        if debt == 0:
            return sum_repaid, month

sum_repaid, month = run_debt(10000, *map(int, input().split()))

print(mformat(sum_repaid))

if "num" in sys.argv:
    print(month)

if "all" in sys.argv:
    for inte in range(1, 100):
        for rep in range(1, 100):
            print(inte, rep)
            smr, _ = run_debt(10000, inte, rep)
            print(smr)
