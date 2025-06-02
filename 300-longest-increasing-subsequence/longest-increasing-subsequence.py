class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        naive solution: generate all possible subsequences, find the max length of subsequence that is
        increasing 
        tc: o(2^n)

        try another approach, for each element, store the current max length of
        a longest increasing subsequence until that element, cache result

        use that cached result to update the LIS of the subsequent elements

        dry run:
        [10,9,2,5,3,7,101,18]
        initialise all LIS of each element to 1
        [1,1,1,1,1,1,1,1]

        for 10, LIS is 1
        for 9, LIS is 1 as 10 > 9
        for 2, LIS is 1 as 10 and 9 > 2
        for 5, since 2 < 5, then LIS of 5 is (1 + LIS of 2) = 2
        [1,1,1,2,1,1,1,1]

        for 3, since 2 < 3, LIS of 3 is (1 + LIS of 2) = 2
        [1,1,1,2,2,1,1,1]

        for 7, since 2, 3, 5 < 7, then LIS of 7 is 1 + max(LIS(2), LIS(3), LIS(5)) = 1 + 2 = 3
        [1,1,1,2,2,3,1,1]

        for 101, since all values < 101, then LIS of 101 is 1 + max(LIS(10), LIS(9),..., LIS(7)) = 1 + 3 = 4
        [1,1,1,2,2,3,4,1]

        for 18, since all values except 101 < 18, then LIS is just 1 + 3 = 4
        [1,1,1,2,2,3,4,4]
        return max of results array which is 4

        possible LIS is 2, 3, 7, 18 or 2, 3, 7, 101
        
        '''
        n = len(nums)
        cache = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    cache[i] = max(cache[i], 1 + cache[j])
        print(cache)

        return max(cache)