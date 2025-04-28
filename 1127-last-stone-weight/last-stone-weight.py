class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, s in enumerate(stones):
            stones[i] = -s
        heapq.heapify(stones)    
        while(len(stones) != 0):
            one = -heapq.heappop(stones)
            if len(stones) == 0:
                return one
            two = -heapq.heappop(stones)
            if one != two:
                new_stone = abs(one-two)
                heapq.heappush(stones, -new_stone)
        if len(stones) == 0:
            return 0
        return -stones[0]