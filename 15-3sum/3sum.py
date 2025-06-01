class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        # [-4 -1 -1 0 1 2]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            current_val = nums[i]
            required_val = 0 - current_val

            left = i + 1
            right = n - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == required_val:
                    temp_array = [nums[i], nums[left], nums[right]]
                    ans.append(temp_array)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr_sum > required_val:
                    right -= 1
                else:
                    left += 1
                    
        return ans