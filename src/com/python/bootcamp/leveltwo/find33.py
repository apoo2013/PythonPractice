# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for index in range(0, len(nums)-1):
        if(nums[index:index+2] == [3,3]):
            return True
    return False