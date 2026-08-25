class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = list() # each element is a tuple (h, i)
        res = 0

        # iterate through the heights
        for i in range(len(heights)):
            h = heights[i]
            if not stk or stk[-1][0] <= h:
                stk.append((h, i))
            else: # current height is lower, and we cannot form a rectangle anymore
                while stk and stk[-1][0] > h:
                    last_h, last_i = stk.pop()
                    res = max(res, last_h * (i - last_i))
                stk.append((h, last_i)) # left extend
        
        # if stack still has element, calculate them again
        rightest_i = len(heights)
        for i in range(len(stk)):
            h, i = stk[i]
            res = max(res, h * (rightest_i - i))

        return res



        