class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        for h in hashmap:
            if hashmap[h] > n//2:
                return h
        
        return -1
            