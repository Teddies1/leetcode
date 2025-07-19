class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s == "":
            return 0

        num_moves = 0
        stack = []

        for parenthesis in s:
            if parenthesis == "(":
                stack.append(parenthesis)
            if parenthesis == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    num_moves += 1


        num_moves += len(stack)
        
        return num_moves