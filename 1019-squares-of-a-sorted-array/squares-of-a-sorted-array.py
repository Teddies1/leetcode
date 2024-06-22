class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        ans = []
        for i in range(len(nums)):
            if abs(nums[left]) < abs(nums[right]):
                ans = [pow(nums[right], 2)] + ans
                right -= 1
            else:
                ans = [pow(nums[left], 2)] + ans
                left += 1
                
                
        return ans