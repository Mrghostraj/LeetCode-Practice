class Solution(object):
    def reverseWords(self, s):
        s = list(s.split())
        s = s[::-1]
        return " ".join(s)