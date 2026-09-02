class Solution(object):
    def isSubsequence(self, s, t):
        first = 0
        sec = 0 
        while sec < len(t) and first < len(s):
            current = s[first]
            if t[sec] == current:
                first +=1
                sec+=1
            else:
                sec+=1
        if first == len(s):
            return True
        return False
            
            

        