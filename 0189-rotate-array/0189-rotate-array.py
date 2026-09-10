class Solution(object): 
    def reverser(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        return nums

    def rotate(self, nums, k):
        k = k%len(nums)
        self.reverser(nums, 0, len(nums)-1)
        self.reverser(nums, 0, k-1)
        self.reverser(nums, k, len(nums)-1)
        return nums
        