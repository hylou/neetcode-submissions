class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = list() # (temp, idx)
        res = [0] * len(temperatures)

        for idx in range(len(temperatures)):
            # If warmer, calcuate idx diff (date) and update result
            while stack and stack[-1][0] < temperatures[idx]:
                t, i = stack.pop()
                res[i] = idx - i
            # if not warmer, append current temperature
            stack.append((temperatures[idx], idx)) 
        return res


            
        