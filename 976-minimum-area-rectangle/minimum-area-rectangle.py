class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set()
        for point in points:
            x, y = point
            point_set.add((x, y))
        ans = float("inf")
        for x1, y1 in point_set:
            for x2, y2 in point_set:
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        ans = min(ans, area)
        return ans if ans != float("inf") else 0