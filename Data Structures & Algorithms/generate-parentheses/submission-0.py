class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = list()
        res = list()

        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                backtrack(opened+1, closed)
                stack.pop() # back to previous state

            if closed < opened:
                stack.append(")")
                backtrack(opened, closed+1)
                stack.pop() # back to previous state

        backtrack(0, 0)
        return res
        