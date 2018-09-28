# Write a function that takes in a list of integers 
# and returns True if it contains 007 in order

def spy_game(nums):
    bond = [0,0,7,'found']
    for x in nums:
        if(x == bond[0]):
            bond.pop(0)
    return bond[0] == 'found'

spy_game([1,0,2,4,0,5,7])
