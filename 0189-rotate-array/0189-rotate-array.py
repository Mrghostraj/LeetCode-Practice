class Solution(object):
    def reverse(self, arr, low, high):
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low +=1
            high -=1
        return arr

    def rotate(self, nums, k):
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

        
        

        