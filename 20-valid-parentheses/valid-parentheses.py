class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)     
            if char == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            if char == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            if char == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
        
        if len(stack) > 0:
            return False
        
        return True