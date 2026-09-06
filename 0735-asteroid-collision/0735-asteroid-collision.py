class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for x in asteroids:
            alive = True
            while stack and stack[-1] > 0 and x < 0:
                if stack[-1] < -x:
                    stack.pop()
                elif stack[-1] > -x:
                    alive = False
                    break 
                else:
                    stack.pop()
                    alive = False
                    break
            if alive:
                stack.append(x)
        return stack

        