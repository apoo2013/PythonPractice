'''
Expressions in O(1) timw
'''

# right propagate the rightmost set bit in x, turns 01010000 to 01011111

def right_prop(x):
    return (x | (x-1))


#compute x mod a power of 2, returns 13 for 77 mod 64
def x_mod_power_2(x, pow2):
    return (x & (pow2 - 1))  #the pow2 has to be the highest power of 2 divisible by x


#test if x is a power of 2, evaluates to true for x = 1, 2, 4, 8...  false for other values