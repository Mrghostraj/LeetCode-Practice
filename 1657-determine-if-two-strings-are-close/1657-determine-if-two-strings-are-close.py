class Solution(object):
    def closeStrings(self, word1, word2):
        freq1 = {}
        freq2 = {}
        for x in word1:
            if x not in freq1:
                freq1[x] = 1
            else:
                freq1[x]+=1
        for x in word2:
            if x not in freq2:
                freq2[x] = 1
            else:
                freq2[x]+=1
        return set(freq1.keys()) == set(freq2.keys()) and  sorted(freq1.values()) == sorted(freq2.values())
        


        