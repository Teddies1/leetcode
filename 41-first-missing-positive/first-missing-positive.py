class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # visited = set()

        # for num in nums:
        #     if num >= 0:
        #         visited.add(num)

        # if not visited:
        #     return 1

        # for i in range(1, max(visited) + 1):
        #     if i not in visited:
        #         return i
        
        # return max(visited) + 1
        n = len(nums)
        i = 0
        while i < n:
            if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != (i + 1):
                return i + 1
        
        return n + 1
        
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]