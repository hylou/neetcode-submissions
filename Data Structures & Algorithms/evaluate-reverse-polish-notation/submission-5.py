class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Process
        # a, b, + -> "a + b" -> c -> push back
        import re
        if len(tokens) == 1:
            return int(tokens[0])
        num_stack = list()
        for item in tokens:
            if bool(re.match(r"^[+-]?\d+$", item)):
                num_stack.append(int(item))
            else:
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                if item == '+':
                    num_stack.append(num1 + num2)
                elif item == '-':
                    num_stack.append(num1 - num2)
                elif item == '*':
                    num_stack.append(num1 * num2)
                else: # '/'
                    num_stack.append(int(float(num1) / num2))
        return num_stack[0]