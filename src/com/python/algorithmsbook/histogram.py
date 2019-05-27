'''
Created on Oct 24, 2018

input: array of int values, and integer m
output: array of length m whose ith entry is the number of times i appeared in the initial array

if values in array are all between 0 and m-1, sum of values in returned array should be equal to a.length

@author: apoorva
'''
import random
def histogram(arr, m):
    result = []

    for j in range(0, m):
        result.append(arr.count(j))
        
    total = 0
    for i in range(len(result)):
        total += result[i]
    if total == len(arr):
        print(f"sum of values in result is {total} and equal to arr length")
    return result

m = 15
arr = []
arrLen = 20
for i in range(0, arrLen):
    arr.append(random.randint(0, m-1))

print(arr)

result = histogram(arr, m)
print(len(result))
print(result)

