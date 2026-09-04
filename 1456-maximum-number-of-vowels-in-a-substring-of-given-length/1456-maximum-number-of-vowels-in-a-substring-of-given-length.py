class Solution(object):
    def maxVowels(self, s, k):
        vowels = 'aeiou'
        count=0
        first =  0
        sec = k-1
        for ch in s[first:sec+1]:
            if ch in vowels:
                count+=1
        vowel_cnt = count

        while sec < len(s)-1:
            if s[first] in vowels:
                count-=1
            if s[sec+1] in vowels:
                count+=1
            first+=1
            sec+=1
            vowel_cnt = max(count, vowel_cnt)
        return vowel_cnt



        