class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        sum1 = (n * (n + 1)) // 2
        sum2 = sum(nums)
        diff = sum1 - sum2
    
        dupe = 0
        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                dupe = nums[i]
                
        return [dupe, dupe + diff]    