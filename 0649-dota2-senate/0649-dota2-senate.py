from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        radiant = deque()
        dire = deque()
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                r = radiant.popleft()
                dire.popleft()
                radiant.append(r+n)
            else:
                r = dire.popleft()
                radiant.popleft()
                dire.append(r+n)
        if radiant:
            return "Radiant"
        else:
            return "Dire"


        