'''
Created on Oct 24, 2018

takes an int value as an argument and returns the largest int not larger than base-2 logarithm of n.
Do not use built-in functions

@author: apoorva
'''

def lg(N):
    if N == 0:
        return -1
    if N == 1:
        return 0
    if N == 2:
        return 1
    difference = N - 2
    track = 2
    counter = 1
    for i in range(0, N):
        track *= 2
        if ((N - track) < difference):
            difference = N - track
        if track > N:
            return counter
        counter += 1
        i += 1
    return 0

print(lg(23))