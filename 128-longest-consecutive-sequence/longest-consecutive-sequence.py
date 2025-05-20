class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set()
        for num in nums:
            number_set.add(num)
        max_length = 0
        for num in number_set:
            if num - 1 not in number_set:
                curr_length = 1
                while num + curr_length in number_set:
                    curr_length += 1
                
                max_length = max(max_length, curr_length)
            
        return max_length