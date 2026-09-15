class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        cnt = 0
        for num in nums:
            if cnt ==0:
                candidate = num
            if candidate == num:
                cnt +=1
            else:
                cnt-=1
        return candidate
        