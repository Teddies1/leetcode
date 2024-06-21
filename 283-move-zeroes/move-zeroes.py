class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        currzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[currzero] = nums[currzero], nums[i]
                currzero += 1
        