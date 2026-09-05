class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0
        total = sum(nums)
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if right_sum == left_sum :
                return i
            left_sum += nums[i]
        return -1

        