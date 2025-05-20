class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        if n == 1:
            return 0 if target == nums[0] else -1

        while left <= right:
            mid = left + (right - left // 2)
            print(mid)
            if target == nums[mid]:
                return mid
            # check if left half is increasing
            elif nums[mid] >= nums[left]:
                # check if target is within left half
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # check if right half is increasing
            else:
                # check if target is within right half
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1