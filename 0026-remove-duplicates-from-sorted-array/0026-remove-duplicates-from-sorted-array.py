class Solution(object):
    def removeDuplicates(self, nums):
        i = 0 
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i+=1
        return i+1

        
        