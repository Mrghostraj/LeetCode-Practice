class Solution(object):
    def productExceptSelf(self, nums):
        product = [1]*len(nums)
        left = 1
        for i in range(len(nums)):
            product[i] = left
            left = left * nums[i]
    
        right = 1
        for i in range(len(nums)-1, -1, -1):
            product[i]= product[i]*right 
            right = right * nums[i]

        return product