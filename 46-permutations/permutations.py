class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        def recurse(nums, visited, ans, path):
            if len(path) == len(nums):
                ans.append(path[:])

            for i in range(len(nums)):
                if i not in visited:
                    path.append(nums[i])
                    visited.add(i)

                    recurse(nums, visited, ans, path)

                    path.pop()
                    visited.remove(i)

        recurse(nums, visited, ans, [])
        return ans