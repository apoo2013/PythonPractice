# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
# and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    total = 0
    allowAdd = True
    for x in arr:
        while allowAdd:
            if x != 6:
                total += x
                break
            else:
                allowAdd = False
        while not allowAdd:
            if x != 9:
                break
            else:
                allowAdd = True
                break
    return total

test = summer_69([2,1,6,9,11])
print(test)     