class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            start, end = intervals[i]
            current_start, current_end = ans[-1]
            if start <= current_end:
                if end > current_end:
                    ans[-1][1] = end
            else:
                ans.append(intervals[i])

        return ans