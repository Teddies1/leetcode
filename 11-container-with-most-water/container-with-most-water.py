class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            ans = max(ans, area)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return ans