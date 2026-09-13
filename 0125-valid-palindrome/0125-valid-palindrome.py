class Solution(object):
    def isPalindrome(self, s):
        res  =""
        s = s.lower()
        for ch in s:
            if ch.isalnum():
                res+=ch
        return res == res[::-1]