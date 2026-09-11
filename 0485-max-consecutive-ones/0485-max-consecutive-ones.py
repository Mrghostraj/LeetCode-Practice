class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                count+=1
                max_count = max(count, max_count)  
                i+=1
            else:
                count = 0
                i+=1
        return max_count
            


            
        