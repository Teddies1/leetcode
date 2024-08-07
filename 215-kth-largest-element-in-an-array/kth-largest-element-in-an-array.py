class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = -num
            
        heapq.heapify(nums)
                
        for i in range(k-1):
            heapq.heappop(nums)
        
        return nums[0] * -1            