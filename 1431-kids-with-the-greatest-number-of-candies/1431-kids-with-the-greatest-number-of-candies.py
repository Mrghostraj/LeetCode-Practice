class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_candy = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result
        
        