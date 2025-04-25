class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        # hashmap = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        # ans = []

        # for key, val in hashmap.items():
        #     if k == 0:
        #         return ans
        #     ans.append(key)
        #     k -= 1

        # return ans

        heap = [(-value, key) for key, value in hashmap.items()]
        heapq.heapify(heap)
        
        ans = []
        for _ in range(k):
            value, key = heapq.heappop(heap)
            ans.append(key)

        return ans