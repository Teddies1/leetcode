class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        
        for char in s:
            if char == "#":
                if len(stack1) != 0:
                    stack1.pop()
            else:
                stack1.append(char)
                
        for char in t:
            if char == "#":
                if len(stack2) != 0:
                    stack2.pop()
            else:
                stack2.append(char)
        print(stack1, stack2)
        return stack1 == stack2