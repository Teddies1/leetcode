class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        idea is to maintain a cumulative sum while iterating through the list
        also maintain a maximum sum, and check if cumulative sum is the new maximum

        since there are negative numbers, reset cumulative sum to 0 if cumulative sum becomes < 0

        dry run
        cumulative sum = -2
        max_sum = 0

        cumulative_sum = 1
        max_sum = 1
        
        cumulative_sum = -2
        max_sum = 1

        cumu_sum = 4
        max_sum = 4

        cumu_sum = 3
        max_sum = 4

        cumu_sum = 5
        max_sum = 5

        cumu_sum = 6
        max_sum = 6

        cumu_sum = 1
        max_sum = 6

        cumu_sum = 5
        max_sum = 6

        return 6
        '''
        max_sum = float("-inf")
        cumulative_sum = 0
        for num in nums:
            cumulative_sum += num
            max_sum = max(cumulative_sum, max_sum)
            cumulative_sum = max(0, cumulative_sum)

        return max_sum