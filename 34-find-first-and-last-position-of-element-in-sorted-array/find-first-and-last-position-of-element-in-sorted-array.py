class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if target not in nums or not nums :
            return ans
        if len(nums) == 1:
            return [0, 0]

        left = self.get_target(nums, target)
        right = self.get_target(nums, target+1)-1

        print(left, right)
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]
    def get_target(self, nums, target):
        n = len(nums)
        left, right = 0, n-1
        ans = n
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    '''
    [5,7,7,8,8,10], target = 8

    mid = 2, nums[mid] = 7
    nums[mid] < target so left = 3

    mid = (5 - 3 / 2) + 3 = 4, nums[mid] = 8
    nums[mid] = target so right = 4, left = 3
    mid = (4-3) / 2 + 3 = 3, nums[mid] = 8
    nums[mid] = target so right = 3, left = 3
    since left == right, end while loop    

    '''