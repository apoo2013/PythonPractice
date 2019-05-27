'''
parity of a word is 1 if number of bits are odd, otherwise it's 0
'''
import time
def parity1(x: int) -> int:
    num = 0
    while x:
        num ^= x & 1
        x >>= 1
    return num 

def parity2(x: int) -> int:
    res = 0
    while x:
        res ^= 1
        x &= (x - 1)
    return res

def parity3(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8 
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
        