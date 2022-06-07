# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prefix = [0] * len(nums)
    postfix = [0] * len(nums)
    ans = [0] * len(nums)
    
    prefix[0] = nums[0]
    postfix[-1] = nums[-1]
    
    i = 1 
    while i < len(nums):
        prefix[i] = prefix[i-1] * nums[i]
        i+=1
    
    i = len(nums) - 2
    while i >= 0:
        postfix[i] = postfix[i+1] * nums[i]
        i-=1
        
    ans[0] = postfix[1]
    ans[-1] = prefix[-2]
    
    i = 1
    while i < len(nums) - 1:
        ans[i] = prefix[i-1] * postfix[i+1]
        i+=1
        
    return ans
