class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        if len(nums) == 1:
            nums[0].sort()
            return nums[0]
        
        set1 = set(nums[0])
        for i in range(1, len(nums)):
            set1 = set1 & set(nums[i])
        
        
        ans = list(set1)
        ans.sort()
        
        return ans