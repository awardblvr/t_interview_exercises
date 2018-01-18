#!/usr/bin/env python

"""
Write a function to determine whether a given number is prime or not (divisible only by
itself and 1). Use the Wikipedia definition of a prime numbers as a reference.
"""

from __future__ import print_function
import sys

def is_prime(val):
    # produce a list of integers > 2 and less than 1/2 of the value
    # produce a list of the None elements which leave remainders 
    # eliminate those elements, and determine length of list to see if prime
    return not bool(len(filter(lambda x: x!=None, [None if (val % x) else x for x in range(2, val/2)])))


if __name__ == '__main__':

    val = int(sys.argv[1])

    print("Is %d Prime:  %r" % (val, is_prime(val)))

    sys.exit()

