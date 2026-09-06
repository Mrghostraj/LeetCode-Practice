class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}
        for x in arr:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x]+=1
        return len(freq.values()) == len(set(freq.values()))

        