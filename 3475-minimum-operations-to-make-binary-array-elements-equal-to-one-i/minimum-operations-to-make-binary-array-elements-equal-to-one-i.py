class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                if i + 1 < n and i + 2 < n:
                    nums[i] = 1
                    nums[i+1] ^= 1
                    nums[i+2] ^= 1
                    ans += 1
        print(nums)

        return ans if 0 not in nums else -1