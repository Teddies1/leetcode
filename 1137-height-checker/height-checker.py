class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        count, n = 0, len(heights)
        expected = sorted(heights)
        print(expected, heights)
        for i in range(n):
            if expected[i] != heights[i]:
                count += 1        
        return count