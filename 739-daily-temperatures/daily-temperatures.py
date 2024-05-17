class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        
        for i in range(n):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            
        # ans = []
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = (j-i)
        #             break
        # while len(ans) != n:
        #     ans.append(0)
        return ans