class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited = set()

        for num in nums:
            if num >= 0:
                visited.add(num)

        if not visited:
            return 1

        for i in range(1, max(visited) + 1):
            if i not in visited:
                return i
        
        return max(visited) + 1