class Solution(object):
    def hIndex(self, citations):
        h =0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h = i+1
            else:
                break
        return h

        