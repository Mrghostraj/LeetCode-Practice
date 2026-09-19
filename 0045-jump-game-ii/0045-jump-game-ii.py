class Solution(object):
    def jump(self, nums):
        steps = 0
        max_range = 0
        current = 0
        for i in range(len(nums)-1):
            max_range = max(max_range, i+nums[i])
            if i == current:
                steps +=1
                current = max_range
        return steps

        