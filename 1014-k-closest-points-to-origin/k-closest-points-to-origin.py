class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, ans = [], []
        
        for point in points:
            distance = pow(point[0], 2) + pow(point[1], 2)
            heapq.heappush(heap, [distance, point])
        
        for i in range(k):       
            item = heapq.heappop(heap)
            ans.append(item[1])
            
        return ans