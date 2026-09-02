class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        right = k-1
        window_sum = sum(nums[0:k])
        max_avg = window_sum/ float(k)
        while right < len(nums)-1:
            window_sum = window_sum - nums[left] + nums[right+1]
            left+=1
            right+=1
            avg = window_sum/ float(k)
            if avg > max_avg:
                max_avg = avg
        return max_avg
        