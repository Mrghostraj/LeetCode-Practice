class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in seen:
                return [seen[comp], i]
            seen[nums[i]] = i

        