class Solution(object):
    def longestOnes(self, nums, k):
        zero_cnt = 0
        left = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt+=1
            if zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -=1
                left+=1
            max_length = max(max_length, right-left+1)
        return max_length
        
        