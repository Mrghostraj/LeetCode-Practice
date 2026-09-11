class Solution(object):
    def singleNumber(self, nums):
        j = 0
        for x in nums:
            j = j^x
        return j

        