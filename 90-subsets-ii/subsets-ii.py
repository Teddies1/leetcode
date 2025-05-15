class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        start from empty list and index
        at each index, can make a choice each time to add or not add
        when we add number, continue recursing by iterating to next index
        terminate when index reaches length of nums
        remove added number to backtrack to other paths
        '''

        ans = []
        nums.sort()
        self.recurse(nums, 0, ans, [])
        return ans

    def recurse(self, nums, index, ans, sub_array):
        # if index is greater than length of nums, completed one branch
        if len(nums) <= index:
            ans.append(sub_array[:])
            return
        # append current number to sub_array
        sub_array.append(nums[index])
        # recursively call next index
        self.recurse(nums, index+1, ans, sub_array)
        # backtrack current choice
        sub_array.pop()

        while index + 1 < len(nums) and nums[index] == nums[index+1]:
            index += 1
        # recurse again after backtracking
        self.recurse(nums, index+1, ans, sub_array) 