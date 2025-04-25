class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        start from empty list and index
        at each index, can make a choice each time to add or not add
        when we add number, continue recursing by iterating to next index
        terminate when index reaches length of nums
        remove added number to backtrack to other paths
        '''

        ans = []
        self.recurse(nums, 0, ans, [])
        return ans

    def recurse(self, nums, index, ans, sub_array):
        if len(nums) <= index:
            ans.append(sub_array[:])
            return

        sub_array.append(nums[index])
        self.recurse(nums, index+1, ans, sub_array)
        sub_array.pop()
        self.recurse(nums, index+1, ans, sub_array)