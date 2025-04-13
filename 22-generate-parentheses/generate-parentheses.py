class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []

        def generate(left, right):
            if left == right == n:
                string = ''.join(stack)
                ans.append(string)
                return
            if left < n:
                stack.append("(")
                generate(left + 1, right)
                stack.pop()
            if right < left:
                stack.append(")")
                generate(left, right + 1)
                stack.pop()
                
        generate(0, 0)
        return ans