class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        stack = []
        leng = 0
        while x:
            
            stack.append(x % 10)
            x //= 10
        
        left, right = 0, len(stack)-1
        while left < right:
            if stack[left] != stack[right]:
                return False
            left += 1
            right -= 1
            
        return True