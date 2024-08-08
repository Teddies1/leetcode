class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        length = len(nums)
        ans = 0
        
        sum_array = []
        
        for i in range(length):
            sum = 0
            for j in range(i, length):
                sum += nums[j]
                sum_array.append(sum)
            
        sum_array.sort()
        for i in range(left-1, right):
            ans += sum_array[i]
            
            
        return ans % (10**9 + 7)