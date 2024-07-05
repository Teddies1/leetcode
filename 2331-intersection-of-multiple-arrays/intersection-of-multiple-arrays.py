class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            nums[0].sort()
            return nums[0]
        
        ans = set(nums[0])
        for i in range(1, len(nums)):
            ans = ans & set(nums[i])
        
        ans = list(ans)
        ans.sort()
        
        return ans