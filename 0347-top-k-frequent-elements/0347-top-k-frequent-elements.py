class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        hashmap = {}
        for num in nums:
            if (num in hashmap):
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for key, value in hashmap.items():
            heapq.heappush(heap, (-value, key))
        print(heap)
        for i in range(k):            
            ans.append(heapq.heappop(heap)[1])
        return ans
            
        
        