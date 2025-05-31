class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        idea is to build and maintain a heap that is heapified based on the euclidean distance (x^2 + y^2)
        once heap is constructed, return the k closest points, which is equal to taking the root, deleting root and heapifying k times
        '''

        heap = []
        ans = []
        for x, y in points:
            euclidean = x**2 + y**2
            heapq.heappush(heap, (euclidean, x, y))

        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])

        return ans