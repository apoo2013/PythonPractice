'''
Created on Oct 24, 2018

Code fragment to print the transposition of a two-dimensional array with m rows and n columns

@author: apoorva
'''
def matTranspose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

mat = [[1,3],[4,6],[7,9]]
trans = matTranspose(mat)

for row in trans:
    print(row)