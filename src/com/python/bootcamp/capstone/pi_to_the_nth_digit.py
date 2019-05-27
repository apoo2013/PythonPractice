'''
Created on Oct 16, 2018

@author: apoorva

Enter a number and have the program generate π (pi) up to that many decimal places. 
Keep a limit to how far the program will go.
'''

from decimal import *

#Maximum precision that can be achieved is 50 decimal digits
getcontext().prec = 50

#use the power series of arctan to calculate pi
#Gregory-Leibnez infinte series
#we know that arctan(1) = pi/4, therefore
#pi/4 = 1 - 1/3 + 1/5 - 1/7 + .....

pibyfour = Decimal(0)
n = 0

while True:
    pibyfour = pibyfour + Decimal(-1) **n /  (Decimal(2*n + 1))
    #    print((pibyfour * Decimal(4)))
    n += 1
print((pibyfour * Decimal(4)))