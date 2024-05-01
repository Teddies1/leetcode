class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                one = int(stack.pop())
                two = int(stack.pop())
                stack.append(one + two)
            elif token == "-":
                one = int(stack.pop())
                two = int(stack.pop())
                stack.append(two - one)
            elif token == "*":
                one = int(stack.pop())
                two = int(stack.pop())
                stack.append(one * two)
            elif token == "/":
                one = int(stack.pop())
                two = int(stack.pop())
                stack.append(two / one)
            else:
                stack.append(token)
        
        return int(stack.pop())