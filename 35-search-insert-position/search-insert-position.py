class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > max(nums):
            return len(nums)
        if target < min(nums):
            return 0
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + ((right - left) // 2)
            if target > nums[mid]:
                left = mid + 1
            elif target <= nums[mid]:
                right = mid - 1
            
        return left