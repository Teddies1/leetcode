class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        for i in range(1, 10):
            self.dfs(i, n, ans)
        return ans

    def dfs(self, number, target, ans):
        if number > target:
            return
        
        ans.append(number)

        for i in range(10):
            new_number = (number * 10) + i
            self.dfs(new_number, target, ans)
        
