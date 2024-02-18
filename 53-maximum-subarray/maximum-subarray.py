class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -(10**4)
        curr = 0
        
        for num in nums:
            curr += num
            ans = max(ans, curr)
            curr = max(0, curr)
        
        return ans 