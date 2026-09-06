class Solution(object):
    def equalPairs(self, grid):
        freq = {}
        
        for row in grid:
            key = tuple(row)
            if key not in freq:
                freq[key] = 1
            else:
                freq[key]+=1
            
        ans = 0
        for j in range(len(grid)):
            column = tuple(grid[i][j] for i in range(len(grid)))
            if column in freq:
                ans+=freq[column]
        return ans
        

        