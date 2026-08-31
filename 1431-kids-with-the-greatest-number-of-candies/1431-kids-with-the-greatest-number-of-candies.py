class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_candy = max(candies)
        for i in range(len(candies)):
            result.append(candies[i]+extraCandies>=max_candy)
        return result
        
        