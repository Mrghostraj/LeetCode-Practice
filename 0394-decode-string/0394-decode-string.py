class Solution(object):
    def decodeString(self, s):
        stack = []
        num = 0
        current = "" 
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch) 
            elif ch == '[':
                stack.append((num, current))

                num = 0
                current = ""
            elif ch.isalpha():
                current+=ch
                
            elif ch =="]":
                prev_num, prev_ch = stack.pop()

                current = prev_ch + prev_num * current
        return current


        