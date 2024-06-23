class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            heapq.heappush(heap, (num * -1))
            
        print(heap)
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        
        return heap[0] * -1            