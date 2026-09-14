class Solution(object):
    def removeDuplicates(self, nums):
        # i = 0 
        # for j in range(len(nums)):
        #     if nums[j] != nums[i]:
        #         nums[i+1] = nums[j]
        #         i+=1
        # return i+1
        k = 0
        for i in range(len(nums)):
            if nums[i] != nums[k]:
                nums[k+1] = nums[i]
                k+=1
        return k+1
        
        