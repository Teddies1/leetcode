class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        
        heap = [(-value, key) for key, value in hashmap.items()]
        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            value, key = heapq.heappop(heap)
            ans.append(key)

        return ans